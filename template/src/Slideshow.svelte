<script lang="ts">
  import { onMount } from "svelte";
  export let sourceUrl: string;

	onMount(() => {
    (window as any).remark.create({ sourceUrl })
  })
</script>
