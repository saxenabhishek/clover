module.exports = {
  apps: [
    {
      name: "FastAPI backend",
      interpreter: "python3",
      interpreter_args: "-m clover",
    },
    {
      name: "Next JS ",
      cwd: "client",
      script: "npm run deploy",
    },
  ],
};
