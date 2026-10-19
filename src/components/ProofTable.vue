<template>
  <section class="proof section">
    <div class="wrap grid">
      <h2 class="head proof-title" data-reveal>
        <span>两个月的</span>
        <span class="proof-indent">建造记录</span>
      </h2>

      <table class="proof-table" data-reveal>
        <caption class="sr-only">四个项目的时间、形态、内容与量化结果</caption>
        <thead class="sr-only">
          <tr>
            <th scope="col">形态</th>
            <th scope="col">项目</th>
            <th scope="col">做了什么</th>
            <th scope="col">数字</th>
          </tr>
        </thead>
        <tbody>
          <tr class="proof-row">
            <td class="proof-shape">桌面</td>
            <td class="proof-name">{{ p0.name }}</td>
            <td class="proof-what">{{ p0.tableResult }}</td>
            <td class="proof-num nums">{{ p0.tableNumber }}</td>
          </tr>
          <tr class="proof-row">
            <td class="proof-shape">群聊</td>
            <td class="proof-name">{{ p1.name }}</td>
            <td class="proof-what">{{ p1.tableResult }}</td>
            <td class="proof-num nums">{{ p1.tableNumber }}</td>
          </tr>
          <tr class="proof-row">
            <td class="proof-shape">插件</td>
            <td class="proof-name">{{ p2.name }}</td>
            <td class="proof-what">{{ p2.tableResult }}</td>
            <td class="proof-num nums">{{ p2.tableNumber }}</td>
          </tr>
          <tr class="proof-row">
            <td class="proof-shape">工具</td>
            <td class="proof-name">{{ p3.name }}</td>
            <td class="proof-what">{{ p3.tableResult }}</td>
            <td class="proof-num nums">{{ p3.tableNumber }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>

<script setup lang="ts">
import { projects } from '../data/projects'

const [p0, p1, p2, p3] = projects as [
  (typeof projects)[number],
  (typeof projects)[number],
  (typeof projects)[number],
  (typeof projects)[number],
]
</script>

<style scoped>
.proof-title {
  grid-column: 1 / 8;
  display: flex;
  flex-direction: column;
  font-size: clamp(2rem, 5vw, 4rem);
  line-height: 1.02;
}

.proof-indent {
  padding-left: 2.2em;
}

.proof-table {
  grid-column: 1 / 13;
  margin-top: 4.5rem;
  width: 100%;
  border-collapse: collapse;
  border: 0;
  text-align: left;
}

.proof-row {
  transition: background-color var(--t-hover) var(--ease-out);
}

.proof-row:nth-child(even) {
  background: var(--surface);
}

.proof-row td {
  padding: 0.95rem 1.25rem;
  vertical-align: baseline;
  font-size: 1rem;
  line-height: 1.5;
}

.proof-shape {
  color: var(--accent);
  font-weight: 600;
  white-space: nowrap;
}

.proof-name {
  color: var(--ink);
  font-weight: 500;
}

.proof-what {
  color: var(--muted);
}

.proof-num {
  color: var(--ink);
  text-align: right;
  white-space: nowrap;
  font-weight: 500;
}

@media (max-width: 900px) {
  .proof-title {
    grid-column: 1 / 13;
  }

  .proof-indent {
    padding-left: 1.1em;
  }

  .proof-table {
    margin-top: 2.5rem;
  }

  .proof-row {
    display: grid;
    grid-template-columns: 1fr auto;
    padding-block: 1rem;
  }

  .proof-row td {
    padding: 0.1rem 0.75rem;
  }

  .proof-shape {
    grid-column: 1;
    font-size: 1.375rem;
    line-height: 1.2;
  }

  .proof-name {
    grid-column: 1;
    font-size: 1.125rem;
  }

  .proof-what,
  .proof-num {
    grid-column: 1 / -1;
    text-align: left;
  }

  .proof-num {
    color: var(--muted);
  }
}
</style>
