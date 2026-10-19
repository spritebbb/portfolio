<template>
  <section class="band">
    <div class="wrap">
      <p class="band-note" data-reveal>
        下面几张不是项目截图，是「把记忆存成可查询的结构」这件事的历史物证。
        我做的事情，和它们隔着一百年，但问的是同一道题。
      </p>
    </div>

    <figure class="band-lead shutter">
      <img
        :src="punched"
        width="1512"
        height="699"
        alt="一张 80 列的穿孔卡片，上面按行列打着方孔，顶部印着一行 Fortran 语句"
        loading="eager"
        decoding="async"
      />
      <figcaption>
        80 列穿孔卡。一条记录就是一张卡，孔打在哪，数据就在哪。查一条记录，得把整箱卡片过一遍机器。
      </figcaption>
    </figure>

    <div class="band-row">
      <figure class="shutter">
        <img
          :src="haspels"
          width="1920"
          height="1081"
          alt="一个打开的纸盒，里面是手写的考古索引卡，卡片顶端有字母分类标签"
          loading="eager"
          decoding="async"
        />
        <figcaption>
          考古学家的索引卡盒：日期、编号、分类、尺寸。四个字段，一条事实，可以按任何一个字段翻。
        </figcaption>
      </figure>

      <figure class="shutter">
        <img
          :src="sorter"
          width="1920"
          height="1453"
          alt="一台机械式穿孔卡分拣机，金属机身，前面是卡片槽"
          loading="eager"
          decoding="async"
        />
        <figcaption>穿孔卡分拣机。它不思考，只负责把对的卡片挑出来。</figcaption>
      </figure>

      <figure class="shutter">
        <img
          :src="library"
          width="1920"
          height="1440"
          alt="图书馆里成排的木质卡片目录柜，抽屉前有金属把手"
          loading="eager"
          decoding="async"
        />
        <figcaption>卡片目录柜。索引的索引——先找到抽屉，再找到卡。</figcaption>
      </figure>
    </div>
  </section>
</template>

<script setup lang="ts">
import punched from '../assets/photos/punched-card.jpg'
import haspels from '../assets/photos/emilie-haspels-index-card-file-wp-20170131.jpg'
import sorter from '../assets/photos/punch-card-sorter.jpg'
import library from '../assets/photos/manchester-central-library-march-2010-4467481691.jpg'
</script>

<style scoped>
.band {
  padding-block: var(--section);
}

.band-note {
  max-width: 46ch;
  color: var(--muted);
  font-size: var(--step-body);
}

.band-lead {
  margin: clamp(2rem, 5vh, 3.5rem) 0 0;
  padding-inline: var(--margin);
}

.band-lead img,
.band-row img {
  width: 100%;
  filter: grayscale(1) sepia(0.3) contrast(1.06) brightness(1.03);
}

.band-lead figcaption,
.band-row figcaption {
  margin-top: 0.9rem;
  font-size: 1rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 46ch;
}

.band-row {
  margin-top: clamp(2rem, 5vh, 3.5rem);
  padding-inline: var(--margin);
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: var(--gutter);
  align-items: start;
}

.band-row figure {
  margin: 0;
}

@media (max-width: 900px) {
  .band-row {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
}
</style>
