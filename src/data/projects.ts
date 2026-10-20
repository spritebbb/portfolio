import demoVideo from '../assets/media/jd-pipeline-demo.mp4'
import demoPoster from '../assets/media/jd-pipeline-poster.jpg'
import botDiagramFlow from '../assets/media/bot-diagram-flow.jpg'
import botDiagramTuple from '../assets/media/bot-diagram-tuple.jpg'
import botDiagramModules from '../assets/media/bot-diagram-modules.jpg'
import dshDiagramFlow from '../assets/media/dsh-diagram-flow.jpg'
import dshDiagramShape from '../assets/media/dsh-diagram-shape.jpg'
import dshDiagramSides from '../assets/media/dsh-diagram-sides.jpg'
import jdDiagramSteps from '../assets/media/jd-diagram-steps.jpg'
import jdDiagramSpec from '../assets/media/jd-diagram-spec.jpg'
import jdDiagramGates from '../assets/media/jd-diagram-gates.jpg'
import cstudyGraph from '../assets/media/cstudy-graph.png'
import cstudyNotes from '../assets/media/cstudy-notes.png'
import cstudySyllabus from '../assets/media/cstudy-syllabus.png'
import tuzhanMain from '../assets/media/tuzhan-assistant-main.jpg'
import tuzhanSettings from '../assets/media/tuzhan-assistant-settings.jpg'
import tuzhanGrowth from '../assets/media/tuzhan-assistant-growth.jpg'

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
  tableShape: string
  tableNumber: string
  stack: string[]
  metrics: Metric[]
  body: Block[]
  pitfall: string
  /** No screenshot: the card shows a text panel instead. */
  textOnly?: boolean
  panel?: { title: string; rows: { k: string; v: string }[] }
  /** Optional real screenshots (first one doubles as the card cover). */
  shots?: string[]
  shotsCaption?: string
  /** Optional demo video and its poster frame. */
  video?: string
  poster?: string
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
    tableShape: '桌面',
    tableResult: '长期记忆与人格系统',
    tableNumber: '432 提交 · 193 项测试',
    poster: tuzhanMain,
    shots: [tuzhanMain, tuzhanSettings, tuzhanGrowth],
    shotsCaption:
      '上面是它现在的界面，从左边起：主聊天页、设置里的数据保护与模型配置、成长总览。',
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
          '这套东西不是一次写成的：记忆系统先在 QQ 机器人上跑过一遍，那边受够了风控和协议变动，搬进桌面端才不用再跟平台较劲。',
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
    slug: 'jd-pipeline',
    name: '管理系统产线',
    en: 'Spring Boot Pipeline',
    tagline: '把「给客户做一套后台系统」这件事，做成一条流水线。',
    period: '2026.09',
    year: '2026',
    repo: 'https://github.com/spritebbb/jd-pipeline',
    tableShape: '产线',
    tableResult: '企业后台生成与交付',
    tableNumber: '30 个脚本 · 五道验收门',
    video: demoVideo,
    poster: demoPoster,
    shots: [jdDiagramSteps, jdDiagramSpec, jdDiagramGates],
    shotsCaption:
      '上面三张不是界面截图，是这条产线自己的图纸：五步怎么串、一份规格长出什么、五道门各查什么。系统跑起来的样子在更上面的视频里。',
    panel: {
      title: '一条流水线，五步把系统交出去',
      rows: [
        { k: '① 换参数', v: 'new-project.mjs 换四个参数，产出一套能直接跑的后台系统' },
        { k: '② 加模块', v: 'new-module.mjs 按 JSON 规格生成 8 个 Java 文件、建表脚本、前端 api 与页面，重复执行结果一致' },
        { k: '③ 体检', v: 'schema-check.mjs 只读检查库表，遇到 DROP 直接拒绝执行' },
        { k: '④ 验收', v: '五道门全在真实浏览器里跑：整页截图、WCAG 对比度、表格溢出、个人中心 18 项、头像上传 12 项' },
        { k: '⑤ 交付', v: 'pack-deploy.mjs 一条命令产出 Windows 与 Linux 包，自带 JRE，客户机不用装 Java' },
      ],
    },
    stack: ['Java 21', 'Spring Boot 3.5', 'MyBatis-Plus', 'MySQL', 'Vue 3', 'Element Plus'],
    metrics: [
      { value: '30', label: '个产线脚本' },
      { value: '5', label: '道真机验收门' },
      { value: '8', label: '个文件一次生成' },
      { value: '1', label: '条命令打包交付' },
    ],
    body: [
      {
        heading: '给一家公司做一个系统不难，难的是做第二家',
        paras: [
          '每次重搭框架、重写登录、重画列表页、重配权限，第二次做出来的和第一次长得不一样，第一个项目修过的 bug 也不会自动进到下一个。',
          '所以把所有项目共用的部分冻结成母版，把每个项目不同的部分变成参数和模块规格：新项目换四个参数，新功能模块写一份 JSON 规格。',
        ],
      },
      {
        heading: '一份 JSON 规格，长出前后端一整条链路',
        paras: [
          '模块生成器读一份规格，产出八个 Java 文件、建表脚本、前端接口文件、页面、路由和菜单项。生成是幂等的，重复跑不会写重，改动被标记块包住，重新生成时不会覆盖手写部分。',
          '生成完脚本自己跑一次库表体检，缺表会报出来。体检脚本只读，遇到 DROP 语句直接拒绝执行：这是防手滑，不是防恶意，它解不了「误删生产库」以外的任何事。',
        ],
      },
      {
        heading: '五道门，全在真实浏览器里跑',
        paras: [
          '截图门、对比度门（WCAG 2.1，正文至少 4.5:1）、表格溢出量测、个人中心 18 项、头像上传 12 项。不用读代码猜，都是打开真实浏览器量出来的。',
          '这五道门挡的是「能用代码证明的错误」。界面贴不贴主题、好不好用，机器判不了，仍然要人眼看截图。这两件事我分得很清楚。',
        ],
      },
    ],
    pitfall:
      '生成器把母版的配置文件原样复制给了每个新项目，于是多个系统共用同一个 JWT 密钥。一个系统签发的 token 可以拿去签另一个系统。这是我自己写出来又自己发现的，正确的做法是生成时给每个项目随机生成密钥。目前它写在 README 的安全说明里，还没改。',
  },  {
    slug: 'cstudy',
    name: 'C 语言备考助手',
    en: 'Cstudy',
    tagline: '把 B 站上的 C 语言课，变成一个会出题、会盯错题的私教。',
    period: '2026.10',
    year: '2026',
    repo: 'https://github.com/spritebbb/Cstudy',
    tableShape: '工具',
    tableResult: '视频转题库',
    tableNumber: '64 个知识点 · 7 题/节',
    poster: cstudyGraph,
    shots: [cstudyGraph, cstudySyllabus, cstudyNotes],
    shotsCaption: '上面是它现在的界面，从左边起：知识图谱、考纲覆盖、笔记。',
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
  {
    slug: 'dsh-skill-usage',
    name: 'DSH 技能中心插件',
    en: 'dsh-skill-usage',
    tagline: '给编辑器加一块面板，看这个会话到底用过哪些技能。',
    period: '2026.09',
    year: '2026',
    repo: 'https://github.com/spritebbb/dsh-skill-usage',
    tableShape: '插件',
    tableResult: 'session projection',
    tableNumber: '3 个版本 · 零额外落库',
    textOnly: true,
    stack: ['TypeScript', 'esbuild', 'session projection'],
    metrics: [
      { value: '3', label: '个版本' },
      { value: '1', label: '个投影' },
      { value: '0', label: '次额外落库' },
      { value: '2', label: '端（host / client）' },
    ],
    shots: [dshDiagramFlow, dshDiagramShape, dshDiagramSides],
    shotsCaption:
      '上面三张是它自己的图纸，不是界面截图：数据怎么流、投影长什么样、两端各做什么。',
    panel: {
      title: '一条记录，从日志流到面板',
      rows: [
        { k: '① 输入', v: 'session log 里的 skill 调用，以及用户 /name 的显式调用' },
        { k: '② 折叠', v: 'skillUsage 投影，纯函数，重放多少次结果都一样' },
        { k: '③ 传输', v: 'host 把投影值折进 list rows，不新开表、不落库' },
        { k: '④ 渲染', v: 'client 用 useSessions 读，画在 sidebar.footer.action' },
        { k: '⑤ 启用', v: '勾选技能后构造一条 /name 提示，让 host 注入全文' },
      ],
    },
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
    slug: 'tuzhan-bot',
    name: '菟菚 QQ bot',
    en: 'TZtuzhan',
    tagline: 'QQ 群里的 AI 伙伴，记得住三个月前说过的话。',
    period: '2026.08',
    year: '2026',
    repo: 'https://github.com/spritebbb/TZtuzhan',
    tableShape: '群聊',
    tableResult: '结构化事实记忆',
    tableNumber: '140 提交 · 195 项测试',
    textOnly: true,
    stack: ['Python', 'NoneBot2', 'SQLite', 'RAG', 'LLM 工具调用'],
    metrics: [
      { value: '195', label: '项 pytest' },
      { value: '140', label: '次提交' },
      { value: '7', label: '个版本' },
      { value: '30+', label: '个功能模块' },
    ],
    shots: [botDiagramFlow, botDiagramTuple, botDiagramModules],
    shotsCaption:
      '上面三张是它自己的图纸，不是界面截图：一条消息怎么被分流、一句话怎么拆成五个字段、三十个模块怎么分组。',
    panel: {
      title: '三十个模块，一个管一件事',
      rows: [
        { k: 'memory', v: '短期对话与人格状态' },
        { k: 'vector_store', v: '本地向量检索，语义召回' },
        { k: 'triple_memory', v: '五元组结构化事实，主体·关系·客体·时间·来源' },
        { k: 'intent', v: '闲聊 / 回忆 / 情感 / 搜索四路分流' },
        { k: 'tool_loop', v: '两轮工具调用迭代，自主决定何时检索' },
        { k: 'affection', v: '好感度四阶段与羁绊' },
        { k: 'mood', v: '心情系统，独立衰减' },
        { k: 'proactive', v: '主动消息与开口时机判断' },
        { k: 'offline_alert', v: '掉线检测、重连与心跳' },
        { k: 'cards', v: '状态卡片渲染成图发回群里' },
      ],
    },
    repoNote:
      '这个项目已经停更：QQ 侧的协议和风控一直在变，bot 反复被平台踢下线，维护精力主要花在对抗平台而不是做功能。同样的记忆系统搬到桌面端就不用再受这些限制，所以重心转到了菟菚桌面助手。代码和 195 项测试都还在仓库里。',
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
