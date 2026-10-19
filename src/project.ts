import { createApp, h } from 'vue'
import ProjectView from './ProjectView.vue'
import { bySlug, nextOf } from './data/projects'
import './styles/tokens.css'
import './styles/base.css'

const slug = document.body.dataset.project ?? ''
const project = bySlug(slug)
const next = nextOf(slug)

createApp({
  render: () => h(ProjectView, { project, next }),
}).mount('#app')
