<script lang="ts">
  export let code: string;
  import type brython from "brython";
  import { onMount } from "svelte";
  import { codeRunLock } from "../store/code-block";

  let editCode: string = code;
  let showEdit: boolean = false;
  let result: string[] = [];
  let currentTime: number = Date.now();

  onMount(() => {
    const interval = setInterval(() => {
      currentTime = Date.now();
    }, 200);
    return () => {
      clearInterval(interval);
    };
  });

  async function runPython(src) {
    // https://groups.google.com/g/brython/c/xLv55qq-L1s
    $codeRunLock = Date.now() + 2000;
    result = [];
    const console_log = console.log;
    // dynamically create an invisible DIV with type="text/python3"
    const pyScript = document.createElement("script");
    pyScript.style.visibility = "hidden";
    (pyScript as any).type = "text/python3";
    // set DIV content to Python source code
    pyScript.textContent = src;
    document.body.appendChild(pyScript);
    // run brython(), searching Python code in DIV tags
    console.log = (x) => (result = [...result, x]);
    brython({ debug: 1 });
    await new Promise((resolve) => setTimeout(resolve, 2000));
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

  .run {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    display: grid;
    grid-template-columns: 1fr 1fr;
    column-gap: 10px;
    background-color: white;
    margin: 10px;
    z-index: 999;
  }

  .code-box {
    display: grid;
    grid-template-rows: 1fr auto;
    row-gap: 5px;
  }
</style>

<div class="toolbar">
  <button
    on:click={() => {
      showEdit = !showEdit;
    }}
    disabled={currentTime < $codeRunLock}>
    Run Code
  </button>
  <a
    target="_blank"
    href="http://pythontutor.com/iframe-embed.html#code={encodeURIComponent(code)}&cumulative=false&py=3">
    <button>Visualize</button>
  </a>
</div>

{#if showEdit}
  <div class="run">
    <div class="code-box">
      <textarea bind:value={editCode} />
      <button
        disabled={currentTime < $codeRunLock}
        on:click={() => {
          runPython(editCode);
        }}>
        Run
      </button>
    </div>
    <div>{result.join('\n')}</div>
  </div>
{/if}
