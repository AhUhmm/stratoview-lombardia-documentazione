export default {
  docSidebar: [
    "intro",
    {
      type: "category",
      label: "Architecture",
      items: ["architecture/complete-architecture", "architecture/user-roles"],
    },
    {
      type: "category",
      label: "Database Schemas",
      items: [
        "schemas/taxonomy-store",
        "schemas/mongodb-schemas",
        "schemas/django-models",
      ],
    },
    {
      type: "category",
      label: "API Documentation",
      items: ["api/api-reference", "api/authentication", "api/endpoints"],
    },
    {
      type: "category",
      label: "Implementation",
      items: [
        "implementation/implementation-guide",
        "implementation/component-architecture",
        "implementation/data-flow",
        "implementation/validation-requirements",
      ],
    },
  ],
};
