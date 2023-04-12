const SIDEBAR_ITEMS = {
  TEXTCLASSIFICATION: [
    {
      id: "annotate",
      tooltip: "Hand labeling",
      icon: "hand-labeling",
      group: "Mode",
      action: "change-view-mode",
      relatedMetrics: ["progress", "stats"],
    },
    {
      id: "labelling-rules",
      tooltip: "Weak labeling",
      icon: "weak-labeling",
      group: "Mode",
      action: "change-view-mode",
      relatedMetrics: ["stats", "rules"],
    },
    {
      id: "explore",
      tooltip: "Exploration",
      icon: "exploration",
      group: "Mode",
      action: "change-view-mode",
      relatedMetrics: ["progress", "stats"],
    },
    {
      id: "progress",
      tooltip: "Progress",
      icon: "progress",
      action: "show-metrics",
      group: "Metrics",
    },
    {
      id: "rules",
      tooltip: "Overall rule metrics",
      icon: "progress",
      action: "show-metrics",
      group: "Metrics",
    },
    {
      id: "stats",
      tooltip: "Stats",
      icon: "stats",
      action: "show-metrics",
      group: "Metrics",
    },
    {
      id: "refresh",
      tooltip: "Refresh",
      icon: "refresh",
      group: "Refresh",
      action: "refresh",
    },
  ],
  TOKENCLASSIFICATION: [
    {
      id: "annotate",
      tooltip: "Hand labeling",
      icon: "hand-labeling",
      group: "Mode",
      action: "change-view-mode",
      relatedMetrics: ["progress", "stats"],
    },
    {
      id: "explore",
      tooltip: "Exploration",
      icon: "exploration",
      group: "Mode",
      action: "change-view-mode",
      relatedMetrics: ["progress", "stats"],
    },
    {
      id: "progress",
      tooltip: "Progress",
      icon: "progress",
      action: "show-metrics",
      group: "Metrics",
    },
    {
      id: "stats",
      tooltip: "Stats",
      icon: "stats",
      action: "show-metrics",
      group: "Metrics",
    },
    {
      id: "refresh",
      tooltip: "Refresh",
      icon: "refresh",
      group: "Refresh",
      action: "refresh",
    },
  ],
  TEXT2TEXT: [
    {
      id: "annotate",
      tooltip: "Hand labeling",
      icon: "hand-labeling",
      group: "Mode",
      action: "change-view-mode",
      relatedMetrics: ["progress", "stats"],
    },
    {
      id: "explore",
      tooltip: "Exploration",
      icon: "exploration",
      group: "Mode",
      action: "change-view-mode",
      relatedMetrics: ["progress", "stats"],
    },
    {
      id: "progress",
      tooltip: "Progress",
      icon: "progress",
      action: "show-metrics",
      group: "Metrics",
    },
    {
      id: "stats",
      tooltip: "Stats",
      icon: "stats",
      action: "show-metrics",
      group: "Metrics",
    },
    {
      id: "refresh",
      tooltip: "Refresh",
      icon: "refresh",
      group: "Refresh",
      action: "refresh",
    },
  ],
  FEEDBACKTASK: [
    {
      id: "annotate",
      tooltip: "Hand labeling",
      icon: "hand-labeling",
      group: "Mode",
      action: "change-view-mode",
      relatedMetrics: ["progress"],
    },
    {
      id: "progress",
      tooltip: "Progress",
      icon: "progress",
      action: "show-metrics",
      group: "Metrics",
    },
    {
      id: "refresh",
      tooltip: "Refresh",
      icon: "refresh",
      group: "Refresh",
      action: "refresh",
    },
  ],
};

Object.freeze(SIDEBAR_ITEMS);
export { SIDEBAR_ITEMS };
