<script lang="ts">
  import { onMount } from "svelte";
  import jQuery from "jquery"
  export let sourceUrl: string;

  let container: HTMLElement;

	onMount(() => {
    (window as any).remark.create({ sourceUrl, container }, () => {
      // callback after creating slides
      jQuery('code.python').each(function(index: number) {
        const node = jQuery(this)
        node.after(`
          <div style="display: flex">
            <a target="_blank" href="https://brython.info/tests/editor.html?lang=en&code=${encodeURIComponent(node[0].innerText)}">
              <button>Run</button>
            </a>
            <a target="_blank" href="http://pythontutor.com/iframe-embed.html#code=${encodeURIComponent(node[0].innerText)}&cumulative=false&py=3">
              <button>Visualize</button>
            </a>
          </div>
        `)
      })
    })
  })
</script>

<div class="container" bind:this={container} />

<style>
  :global(body) {
    padding: 0px;
  }
  .container {
    width: 100%;
    height: 100%;
  }
</style>