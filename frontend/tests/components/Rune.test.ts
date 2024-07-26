import { beforeEach, afterEach, describe, expect, test, vi } from "vitest";
import { mount, VueWrapper } from "@vue/test-utils";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import Rune from "@/components/Rune.vue";
import { RuneType } from "@/types/RuneType";
import { createPromiseClient } from "@connectrpc/connect";

describe("Rune", () => {
  let wrapper: VueWrapper;

  vi.mock("@connectrpc/connect", async () => {
    const mockClient = {
      update: vi.fn().mockResolvedValue({ data: "Mocked Data" }),
    };

    return {
      createPromiseClient: vi.fn(() => mockClient),
    };
  });

  function mountWrapper(rune: RuneType) {
    wrapper = mount(Rune, {
      global: {
        plugins: [createVuetify({ components, directives })],
      },
      props: {
        rune: rune,
      },
    });
  }

  afterEach(() => {
    vi.restoreAllMocks();
  });

  test("should render correctly", async () => {
    // Given
    mountWrapper(new RuneType("Test", 1000, 100, 10));

    // Then
    expect(wrapper.get("[data-testid=rune-name]").text()).toBe("Rune Test");
    expect(wrapper.props("rune")).toEqual({
      name: "Test",
      prixBa: 10,
      prixPa: 100,
      prixRa: 1000,
    });
  });

  test("update prix Ra", async () => {
    // Given
    mountWrapper(new RuneType("Test", 1000, 100, 10));

    // When
    const input = wrapper.find('[data-testid="prix-ra"] input');
    await input.setValue("456");
    await input.trigger("change");

    // Then
    expect(createPromiseClient().update).toHaveBeenCalledWith({
      name: "Test",
      prixBa: 10,
      prixPa: 100,
      prixRa: "456",
    });
  });

  test("update prix Pa", async () => {
    // Given
    mountWrapper(new RuneType("Test", 1000, 100, 10));

    // When
    const input = wrapper.find('[data-testid="prix-pa"] input');
    await input.setValue("123");
    await input.trigger("change");

    // Then
    expect(createPromiseClient().update).toHaveBeenCalledWith({
      name: "Test",
      prixBa: 10,
      prixPa: 123,
      prixRa: 1000,
    });
  });

  test("update prix Ba", async () => {
    // Given
    mountWrapper(new RuneType("Test", 1000, 100, 10));

    // When
    const input = wrapper.find('[data-testid="prix-ba"] input');
    await input.setValue("789");
    await input.trigger("change");

    // Then
    expect(createPromiseClient().update).toHaveBeenCalledWith({
      name: "Test",
      prixBa: 789,
      prixPa: 100,
      prixRa: 1000,
    });
  });

  test("hide non relevant rune level", async () => {
    // Given
    mountWrapper(new RuneType("Test", -1, -1, -1));

    // Then
    expect(wrapper.find('[data-testid="prix-ra"]').exists()).toBe(false);
    expect(wrapper.find('[data-testid="prix-pa"]').exists()).toBe(false);
    expect(wrapper.find('[data-testid="prix-ba"]').exists()).toBe(false);
  });
});
