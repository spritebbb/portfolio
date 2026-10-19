/**
 * "One decision, a set of numbers" — the part of each project a technical
 * interviewer actually wants to poke at: what was on the table, what got
 * ruled out, and what the numbers said.
 *
 * Every figure here is traceable to the project's own README or repo stats.
 * Nothing is estimated, rounded up, or invented.
 */

export interface DecisionFigure {
  v: string
  l: string
}

export interface Decision {
  question: string
  options: string[]
  call: string
  figures: DecisionFigure[]
}

export const decisions: Record<string, Decision> = {
  'tuzhan-assistant': {
    question: '记忆层自己写，还是接一个现成的？',
    options: [
      '接 Mem0：现成的记忆方案，装上一个包就能跑',
      '自己写：SQLite + 本地向量检索，来源和置信度都由自己管',
    ],
    call: '先让 Mem0 跑了一版，用同一批问题测第一顺位召回：hit@1 是 0.45。自建的版本在同一批问题上做到 0.85。差出来的不是"能不能搜到"，是"搜到的对不对"。所以那条 Mem0 分支留着当对照，但默认关闭。',
    figures: [
      { v: '0.45', l: 'Mem0 的 hit@1' },
      { v: '0.85', l: '自建记忆的 hit@1' },
      { v: '193', l: '项回归测试守着这个数' },
    ],
  },

  'tuzhan-bot': {
    question: '一句话，存成一段文本还是拆成一条记录？',
    options: [
      '整句进向量库：检索最省事，相似度一算就出结果',
      '拆成五元组：主体、关系、客体、时间、来源，各占一个字段',
    ],
    call: '整句方案有个绕不过去的麻烦：她上周说讨厌香菜、今天说想试试，两句话在向量空间里几乎重合，检索出来是打架的。拆成五元组之后，两件事各是一条记录，主语和时间都在字段里，检索可以按主体筛、按时间排序，"改主意"这件事本身就能被表达出来。',
    figures: [
      { v: '5', l: '个字段构成一条记忆' },
      { v: '30+', l: '个模块围着它长出来' },
      { v: '195', l: '项 pytest 跑在每次改动前' },
    ],
  },

  'dsh-skill-usage': {
    question: '技能使用记录，另存一份还是从日志里折出来？',
    options: [
      '新开一张表：面板读起来最直接',
      '注册 session projection：对已有的 session log 做纯函数折叠',
    ],
    call: 'session log 里已经记了每一次技能调用。再存一份就是两份真相，早晚会对不上。projection 是纯函数：同一条日志重放多少次，折出来的结果都一样，所以面板不需要"同步"这个动作，也不会有面板数据和日志对不上这种 bug。代价是每次读都要现算，但这个量级完全付得起，换来的是零额外落库。',
    figures: [
      { v: '1', l: '个 projection 撑起整个面板' },
      { v: '0', l: '张新增的表' },
      { v: '3', l: '个版本迭代出来' },
    ],
  },

  cstudy: {
    question: '知识图谱的连线，AI 直接写库还是人拍板？',
    options: [
      'AI 直接入库：打开就有图，体验最顺',
      'AI 提议，弹窗逐条确认：多一步点击',
    ],
    call: '一张画错的图比没有图更糟：你会拿着一个错的结构去复习，而且看不出来它错在哪。所以连线由模型提，但每一条都要在弹出的窗口里点确认才进库。这一步点击不是防模型，是防自己在不知情的情况下信了模型。',
    figures: [
      { v: '64', l: '个考纲知识点' },
      { v: '7', l: '题每节课自动出' },
      { v: '6', l: '条验收标准写在 README' },
    ],
  },
}
