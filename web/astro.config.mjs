import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://clearmarket.fyi',
  output: 'static',
  build: {
    inlineStylesheets: 'auto',
  },
  compressHTML: true,
});
