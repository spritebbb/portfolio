<template>
  <div class="page">
    <SiteHero />
    <main>
      <WorkIndex />
      <MemoryBand />
      <ProofTable />
      <MemoryDemo />
      <AboutCopy />
    </main>
    <SiteContact />
  </div>
  <SiteFooter />
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import SiteHero from './components/SiteHero.vue'
import WorkIndex from './components/WorkIndex.vue'
import ProofTable from './components/ProofTable.vue'
import MemoryDemo from './components/MemoryDemo.vue'
import MemoryBand from './components/MemoryBand.vue'
import AboutCopy from './components/AboutCopy.vue'
import SiteContact from './components/SiteContact.vue'
import SiteFooter from './components/SiteFooter.vue'
import { initReveal } from './lib/reveal'

onMounted(() => {
  initReveal()
})
</script>

<style scoped>
.page {
  position: relative;
  z-index: 1;
  background: var(--bg);
}
</style>
