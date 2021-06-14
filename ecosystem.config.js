module.exports = {
  apps: [
    {
      name: "FastAPI backend",
      interpreter: "python",
      interpreter_args: "-m clover",
    },
    {
      name: "Next JS ",
      cwd: "client",
      script: "npm run deploy",
    },
  ],
};
