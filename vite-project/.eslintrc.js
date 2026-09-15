module.exports = {
  "languageOptions": {
    ecmaVersion: 2021,
    sourceType: "module",
    globals: {
      window: "readonly",
      process: "readonly",
      console: "readonly",
      browser: "readonly"
    },
  },
  overrides: [
    {
      files: ['*.ts', '*.tsx'],
      parserOptions: {
        project: './tsconfig.json',
      },
    },
  ],
  languageOptions: {
    ecmaVersion: 2021,
    sourceType: "module",
    globals: {
      window: "readonly",
      process: "readonly",
      console: "readonly",
      browser: "readonly"
    },
  },

  extends: [
  'eslint:recommended',
  'plugin:react/recommended',
  'plugin:@typescript-eslint/recommended',
  'prettier',
  {
    files: ['*.ts', '*.tsx'],
    parserOptions: {
      project: './tsconfig.json',
    },
  },
  // Add custom rules here
  ],
  parser: '@typescript-eslint/parser',
  settings: {
    react: {
      version: 'detect'
    }
  },

  parserOptions: {
    ecmaFeatures: {
      jsx: true,
    },
    ecmaVersion: 12,
    sourceType: 'module',
  },
  plugins: ['react', '@typescript-eslint'],
  rules: {
        'no-console': 'warn',
    'react/react-in-jsx-scope': 'off',
    'react/prop-types': 'off',
    // Add custom rules here
  },
};
