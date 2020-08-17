import type JQuery from 'jquery'
import { writable } from 'svelte/store'
import type { Writable } from 'svelte/store'

export interface CodeBlockInfo {
  code: string
  ref: HTMLElement
  node: JQuery<HTMLElement>
}

export const codeBlockInfos: Writable<CodeBlockInfo[]> = writable([])