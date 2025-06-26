const config = {
  title: "Stratoview Documentation",
  tagline: "Complete Technical Documentation",
  favicon: "img/favicon.ico",
  url: "https://stratoview-lombardia.netlify.app",
  baseUrl: "/",

  // Previeni indicizzazione
  noIndex: true,

  organizationName: "IZILab",
  projectName: "stratoview-lombardia-docs",

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",

  i18n: {
    defaultLocale: "it",
    locales: ["it"],
  },

  // Abilita Mermaid
  markdown: {
    mermaid: true,
  },
  themes: ["@docusaurus/theme-mermaid"],

  presets: [
    [
      "classic",
      {
        docs: {
          routeBasePath: "/", // Docs alla root
          sidebarPath: "./sidebars.js",
          editUrl:
            "https://github.com/ahuhmm/stratoview-lombardia-documentazione/tree/main/",
        },
        blog: false, // Disabilita blog
        theme: {
          customCss: "./src/css/custom.css",
        },
      },
    ],
  ],

  plugins: ["@r74tech/docusaurus-plugin-panzoom"],

  themeConfig: {
    // Mermaid con zoom/pan
    mermaid: {
      theme: { light: "light", dark: "default" },
      options: {
        maxTextSize: 100000, // Per diagrammi grandi
      },
    },

    // SEO - non indicizzare
    metadata: [{ name: "robots", content: "noindex, nofollow" }],

    navbar: {
      title: "Stratoview Lombardia",
      /* logo: {
        alt: "Stratoview Logo",
        src: "img/logo.svg",
      }, */
      items: [
        {
          type: "docSidebar",
          sidebarId: "docSidebar",
          position: "left",
          label: "Documentation",
        },
        {
          href: "/mockup",
          label: "🚀 Interactive Demo",
          position: "left",
        },
        {
          href: "/documentation-strategy",
          label: "Documentation Strategy",
          position: "left",
        },
      ],
    },

    footer: {
      style: "dark",
      copyright: `Copyright © ${new Date().getFullYear()} Stratoview. Built with Docusaurus.`,
    },

    prism: {
      theme: require("prism-react-renderer").themes.github,
      darkTheme: require("prism-react-renderer").themes.dracula,
      additionalLanguages: ["json", "python", "mongodb"],
    },
  },
};

module.exports = config;
