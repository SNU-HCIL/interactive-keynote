<script lang="ts">
  export let code: string;
  import type brython from "brython";
  import { onMount } from "svelte";

  let result: string[] = []

  async function runPython(src){
    result = []
    const console_log = console.log
    // dynamically create an invisible DIV with type="text/python3"
    const pyScript = document.createElement('script');
    pyScript.style.visibility = 'hidden';
    (pyScript as any).type = 'text/python3';
    // set DIV content to Python source code
    pyScript.textContent = src;
    document.body.appendChild(pyScript);
    // run brython(), searching Python code in DIV tags
    console.log = x => result = [...result, x]
    brython({debug:1});
    await new Promise(resolve => setTimeout(resolve, 2000))
    console.log = console_log;
    // clean up
    document.body.removeChild(pyScript);
  }

</script>

<style>
  .toolbar {
    display: flex;
    justify-content: flex-end;
  }

  .toolbar button {
    margin-top: 10px;
    margin-left: 10px;
    font-family: "Quattrocento Sans";
  }
</style>

<div class="toolbar">
  <button
    on:click={() => runPython(code)}
  >Run</button>
  <a
    target="_blank"
    href="http://pythontutor.com/iframe-embed.html#code={encodeURIComponent(code)}&cumulative=false&py=3">
    <button>Visualize</button>
  </a>
</div>

<div>
  {result.join('\n')}
</div>