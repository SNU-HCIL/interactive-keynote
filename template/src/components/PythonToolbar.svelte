<script lang="ts">
  export let code: string
</script>

<div style="display: block">
  <a target="_blank"
    href="https://brython.info/tests/editor.html?lang=en&code={encodeURIComponent(code)}"
  >
    <button>Run</button>
  </a>
  <a target="_blank"
    href="http://pythontutor.com/iframe-embed.html#code={encodeURIComponent(code)}&cumulative=false&py=3"
  >
    <button>Visualize</button>
  </a>
</div>

<style>
  a {
    float: right;
  }

  button {
    margin-top: 10px;
    margin-left: 10px;
    font-family: 'Quattrocento Sans';
  }

</style>