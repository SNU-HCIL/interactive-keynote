<script lang="ts">
  import type brython from "brython";
  import { onMount } from "svelte";
  import { codeRunLock } from "../store/code-block";
  import {
    Row,
    Col,
    Input,
    Button,
    Modal,
    ModalBody,
    ModalFooter,
    ModalHeader,
  } from "sveltestrap";

  export let code: string;
  let editCode: string = code;
  let showEdit: boolean = false;
  const toggle = () => (showEdit = !showEdit);
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
    const timeout = 2000;
    // https://groups.google.com/g/brython/c/xLv55qq-L1s
    $codeRunLock = Date.now() + timeout;
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
    console.log = (x) => (result = [...result, x.trim()]);
    brython({ debug: 1 });
    await new Promise((resolve) => setTimeout(resolve, timeout));
          // console.log = console_log;
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

  .code-result {
    white-space: pre-wrap;
    height: 100%;
    max-height: 465px;
    overflow: scroll;
    padding: 10px;
  }
</style>

<div class="toolbar">
  <button
    on:click={() => {
      showEdit = true;
      editCode = code
      runPython(editCode);
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

<div
  on:keydown|stopPropagation={() => {}}
  on:keypress|stopPropagation={() => {}}
  on:mousewheel|stopPropagation={() => {}}
>
  <Modal 
    isOpen={showEdit} {toggle} transitionOptions={{}} size="lg">
    <ModalHeader {toggle}>
      <span>Code Editor</span>
      <span class="text-muted ml-3"><small>powered by <a class="text-color-secondary" href="https://brython.info/">Brython</a></small></span>
    </ModalHeader>
    <ModalBody>
      <Row style={`height: 450px`}>
        <Col xs="6">
          <textarea
            style="width: 100%; height: 100%"
            bind:value={editCode} />
        </Col>
        <Col xs="6">
          <p class="code-result bg-light">{result.join('\n')}</p>
        </Col>
      </Row>
    </ModalBody>
    <ModalFooter>
      <Button
        color="primary"
        disabled={currentTime < $codeRunLock}
        on:click={() => {
          runPython(editCode);
        }}>
        Run
      </Button>
      <Button color="secondary" on:click={toggle}>Cancel</Button>
    </ModalFooter>
  </Modal>
</div>