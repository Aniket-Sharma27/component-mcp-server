module.exports = {
  apps: [
    {
      name: "component-mcp-server",
      script: "dist/http.js",
      cwd: __dirname,
      instances: 1,
      exec_mode: "fork",
      autorestart: true,
      max_restarts: 10,
      restart_delay: 2000,
      watch: false,
      env: {
        NODE_ENV: "production",
      },
      out_file: "logs/out.log",
      error_file: "logs/error.log",
      log_date_format: "YYYY-MM-DD HH:mm:ss Z",
      merge_logs: true,
    },
  ],
};
