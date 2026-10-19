export interface Metric {
  value: string
  label: string
}

export interface Block {
  heading: string
  paras: string[]
  points?: string[]
}

export interface Project {
  slug: string
  name: string
  en: string
  tagline: string
  period: string
  year: string
  repo: string
  tableResult: string
  tableNumber: string
  stack: string[]
  metrics: Metric[]
  body: Block[]
  pitfall: string
  /** Optional line about the repo's current state (e.g. mid-rewrite). */
  repoNote?: string
}

export const projects: Project[] = [
  {
    slug: 'tuzhan-assistant',
    name: '菟菚桌面助手',
    en: 'TZtuzhanAssistant',
    tagline: '一个装在桌面上、会记事也会忘事的 AI 伙伴。',
    period: '2026.09',
    year: '2026',
    repo: 'https://github.com/spritebbb/TZtuzhanAssistant',
    tableResult: '长期记忆与人格系统',
    tableNumber: '432 提交 · 193 项测试',
    stack: ['Python', 'FastAPI', 'Vue 3', 'SQLite', 'SSE', 'MCP'],
    metrics: [
      { value: '432', label: '次提交' },
      { value: '193', label: '项回归测试' },
      { value: '6', label: '个发布版本' },
      { value: '51', label: '版数据库 schema' },
    ],
    repoNote:
      '仓库当前在重构：功能完整的稳定版是 tag v3.6.0，上面这些数字全部出自那一版；main 正在拆掉冗余模块，暂时不完整。',
    body: [
      {
        heading: '记忆不是一段文本，是一条有出处的记录',
        paras: [
          '大多数「AI 记忆」的做法是把聊天记录摘要一下再塞回 prompt。问题是摘要会丢来源，丢了来源就没人能判断它该不该信。',
          '这里的每条记忆落进 SQLite 时都带着四样东西：哪次对话说的、谁说的、多确定、什么时候说的。取用的时候走本地向量检索，相关的几条连同出处一起交给模型。',
        ],
        points: [
          '用户可以点名纠正一条记忆，纠正会覆盖旧值但留下改动痕迹，不是悄悄替换。',
          '没有被再次强化的记忆按时间衰减，被反复提到的自动加固。',
          '可以给某条记忆打上固定保留，让它不参与衰减。',
        ],
      },
      {
        heading: '记忆会互相打架，所以要有裁判',
        paras: [
          '同一个人的说法过三个月就变了。系统如果只会新增，最后会同时相信两个互相矛盾的版本，而且两个都「有出处」。',
          '所以记忆写入前要过三道岗：新说法和旧说法矛盾时，判定是演化（旧条目标记被取代、保留演化链）还是补充佐证（加固旧条目）；用户画像变了，旧画像归档而不是删除；她自己的自述前后不一致时，让模型把这个矛盾讲清楚，而不是二选一。',
        ],
      },

    ],
    pitfall:
      'v3.5 做完一轮全量排查，103 个问题清到零：P0 一个、P1 十三个、P2 二十一个、P3 六十八个。教训是 AI 产品的 bug 大多不在报错里，在「它记得，但记错了」。',
  },
  {
    slug: 'tuzhan-bot',
    name: '菟菚 QQ bot',
    en: 'TZtuzhan',
    tagline: 'QQ 群里的 AI 伙伴，记得住三个月前说过的话。',
    period: '2026.08',
    year: '2026',
    repo: 'https://github.com/spritebbb/TZtuzhan',
    tableResult: '结构化事实记忆',
    tableNumber: '140 提交 · 195 项测试',
    stack: ['Python', 'NoneBot2', 'SQLite', 'RAG', 'LLM 工具调用'],
    metrics: [
      { value: '195', label: '项 pytest' },
      { value: '140', label: '次提交' },
      { value: '7', label: '个版本' },
      { value: '30+', label: '个功能模块' },
    ],
    repoNote:
      '这个项目已经停更：QQ 侧的协议和风控一直在变，bot 反复被平台踢下线，维护精力主要花在对抗平台而不是做功能。同样的记忆系统搬到桌面端就不用再受这些限制，所以重心转到了第一个项目。代码和 195 项测试都还在仓库里。',
    body: [
      {
        heading: '五元组：把聊天变成能查的事实',
        paras: [
          '聊天记录是流水，事实是结构。每句值得记的话被拆成主语、关系、宾语、时间、来源五个字段入库，检索时按字段查，而不是把整段聊天塞进 prompt。',
          '配合意图路由，四种问法走四条路：闲聊不检索、回忆查五元组、情感走关系数据、搜索走联网。只有「回忆」这一类才真的触发 RAG。',
        ],
        points: [
          '问「我上次说的那个游戏」能查出来，因为游戏名作为宾语存在一张表里。',
          '同一个事实被重复提到，置信度累加；被否定，标记失效而不是删除。',
        ],
      },
      {
        heading: '会掉线、会被风控，所以要有脉搏',
        paras: [
          'QQ 侧的 bot 不是写完就能一直跑的。消息频率、登录态、掉线重连，每一样都会在半夜出问题。',
        ],
        points: [
          '发消息带延迟抖动，避免固定节奏被判定成机器人。',
          '掉线检测加离线告警，断了会喊人。',
          '健康自检脚本一次看三样：进程在不在、WebSocket 通不通、日志有没有连续报错。',
          'Web 管理面板跑在独立进程上，bot 崩了面板还活着，方便上去看。',
        ],
      },
      {
        heading: '主动说话比被动回答难',
        paras: [
          '被问才答是容易的；知道什么时候该开口才是难的部分。',
          '今日日程由模型生成，节日表同时覆盖公历和农历，主动消息的时机由好感度阶段和情绪状态决定，不是定时群发。状态查询命令出的是图片卡片，不是一坨文字。',
        ],
      },
    ],
    pitfall:
      '第一版把所有上下文都往 prompt 里塞，token 炸了，答得还更差。改成意图路由加五元组检索之后，同样的问题 prompt 短了一个数量级，准确率反而上去了。',
  },
  {
    slug: 'dsh-skill-usage',
    name: 'DSH 技能中心插件',
    en: 'dsh-skill-usage',
    tagline: '给编辑器加一块面板，看这个会话到底用过哪些技能。',
    period: '2026.09',
    year: '2026',
    repo: 'https://github.com/spritebbb/dsh-skill-usage',
    tableResult: 'session projection',
    tableNumber: '3 个版本 · 零额外落库',
    stack: ['TypeScript', 'esbuild', 'session projection'],
    metrics: [
      { value: '3', label: '个版本' },
      { value: '1', label: '个投影' },
      { value: '0', label: '次额外落库' },
      { value: '2', label: '端（host / client）' },
    ],
    repoNote:
      '这个插件停在 v0.2.0：它要解决的问题后来官方有了更好的方案，所以不再单独维护。留下来的是当初那个判断，用 session projection 折出使用记录，而不是另存一张表。',
    body: [
      {
        heading: '输入是会话日志，输出是面板要的那两个值',
        paras: [
          '一个 session projection：输入是会话日志，输出是「当前用过的技能」和「历史调用」。纯 fold，不写库、不发请求、不改会话。宿主在返回会话列表时把这个投影的值一起折进去，前端直接读。',
          '所有代价都在这儿：每次读都要现算。所有收益也在这儿：没有第二份真相，也就没有「面板和日志对不上」这种 bug。',
        ],
      },
      {
        heading: '两半：宿主一个 fold，前端一个座位',
        paras: [
          '宿主侧只关心两种事件：模型调用 skill 工具，以及用户手输 /技能名 显式调用。两者都折叠成同一个结构。',
          '前端侧通过全局的会话 seat 读投影值，渲染在侧边栏底部的动作带上。点开能看到已用技能和本会话可用的技能目录。',
          '里面的「启用」不会改任何状态，它只构造一条装载指令，交给宿主去注入技能正文，这样插件的权限边界始终是只读的。',
        ],
      },
    ],
    pitfall:
      'projection 听起来像 hook，其实它是纯函数。想清楚「我要的是派生结果还是副作用」，代码能少一半，这个插件最后只有两个文件。',
  },
  {
    slug: 'cstudy',
    name: 'C 语言备考助手',
    en: 'Cstudy',
    tagline: '把 B 站上的 C 语言课，变成一个会出题、会盯错题的私教。',
    period: '2026.10',
    year: '2026',
    repo: 'https://github.com/spritebbb/Cstudy',
    tableResult: '视频转题库',
    tableNumber: '64 个知识点 · 7 题/节',
    stack: ['Python', 'PyQt6', 'SQLite', 'whisper', 'LLM'],
    metrics: [
      { value: '64', label: '个考纲知识点' },
      { value: '7', label: '题每节课' },
      { value: '6', label: '条验收标准' },
      { value: '1', label: '次点击打包' },
    ],
    body: [
      {
        heading: '一条流水线：视频 → 笔记 → 题',
        paras: [
          '粘贴一个 B 站链接，后面全是自动的：抓字幕（没有 CC 就用本地 whisper 转写）、按十分钟切块逐块总结再合并、生成 Markdown 笔记、基于笔记出题、落库。',
          '每节课固定出七道题：三道选择、两道填空、一道阅读、一道编程，每题带答案和解析。刷题界面可以按题型、章节、来源挑，也可以按考试分值比例组一套真题。',
        ],
      },
      {
        heading: '字幕里没有代码，所以去看屏幕',
        paras: [
          '老师讲「这里我们写一个循环」的时候，循环本身在屏幕上，不在字幕里。只靠字幕生成的笔记，满篇都是这种指代不明的句子。',
          '加了一步关键帧读屏：定时截取视频画面，把屏幕上的代码和 PPT 读进笔记。代码块终于出现在该出现的位置。',
        ],
      },
      {
        heading: '一张图，看得见自己哪块没学会',
        paras: [
          '图谱里圆圈大小是题量，颜色是我自己的正确率，连线是两个知识点之间的关系。所以在图上找「红的大圈」就成了找弱点：题目多、但我错得多的地方。',
          '连线不是自动长出来的，每一条都过了人手（为什么非得这样，前面那栏写了）。',
        ],
      },
    ],
    pitfall:
      '第一版把出题和写笔记放在同一次模型调用里，结果题和笔记互相污染，笔记质量先垮了。拆成两步之后笔记稳住了题才跟着准，README 里那六条验收标准就是被这次返工逼出来的。',
  },
]

export const bySlug = (slug: string): Project => {
  const found = projects.find((p) => p.slug === slug)
  if (!found) throw new Error(`unknown project: ${slug}`)
  return found
}

export const nextOf = (slug: string): Project => {
  const i = projects.findIndex((p) => p.slug === slug)
  return projects[(i + 1) % projects.length]!
}
