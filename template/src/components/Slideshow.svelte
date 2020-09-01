<script lang="ts">
  import { onMount, afterUpdate } from "svelte";
  import { codeBlockInfos } from '../store/code-block'
  import jQuery from "jquery"
  import PythonToolbar from "./PythonToolbar.svelte";
  export let sourceUrl: string;

  let container: HTMLElement;

	onMount(() => {
    (window as any).remark.create({ sourceUrl, container }, () => {
      // callback after creating slides
      const selection = jQuery('.remark-slides-area code.python')
      $codeBlockInfos = selection.map(function() {
        const node = jQuery(this)
        return {
          ref: null,
          node,
          code: node.children().toArray().map(codeLineDiv => codeLineDiv.innerText).join('\n')
        }
      }).toArray()

      const slides = jQuery('.remark-slide-content')
      console.log(slides);

      let imgStr;

      slides.append("<img class='logo' width='100px' style='position:absolute; right: 15px; top: 15px;' src='img/hcilogo_snu.png'/>");

    })
  })

  codeBlockInfos.subscribe(() => {
    $codeBlockInfos.forEach(block => {
      block.node.after(block.ref)
    })
  })
</script>

<div class="container-fluid" bind:this={container} />

<!--
  Mimic React's dynamic component rendering behavior
  1. get the required number of components
  2. render svelte components using #each directive
  3. bind all rendered components to JS variable
  4. move them into desired space by direct manipulating DOM at afterUpdate
-->
{#each $codeBlockInfos as block }
  <div bind:this={block.ref}>
    <PythonToolbar code={block.code} />
  </div>
{/each}

<style>
  :global(body) {
    padding: 0px;
  }
  .container-fluid {
    height: 100%;
  }
</style>
