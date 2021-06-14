module.exports = {
  apps: [
    {
      name: "FastAPI backend",
      interpreter: "/bin/bash",
      script: "flaskapi.sh",
    },
    {
      name: "Next JS ",
      cwd: "client",
      script: "npm run deploy",
    },
  ],
};
