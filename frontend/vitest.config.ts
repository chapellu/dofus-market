import { defineConfig, mergeConfig } from "vite";
import viteConfig from "./vite.config";
import { configDefaults } from "vitest/config";

export default mergeConfig(
  viteConfig,
  defineConfig({
    test: {
      globals: true,
      environment: "happy-dom",
      server: {
        deps: {
          inline: ["vuetify"],
        },
      },
      coverage: {
        reporter: ["text", "lcov"],
      },
    },
  })
);
