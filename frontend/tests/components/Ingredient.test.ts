import { afterEach, describe, expect, test, vi } from "vitest";
import { mount, VueWrapper } from "@vue/test-utils";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import { createPromiseClient } from "@connectrpc/connect";
import Ingredient from "@/components/Ingredient.vue";

describe("Ingredient", () => {
  vi.mock("@connectrpc/connect", async () => {
    const mockClient = {
      update: vi.fn().mockResolvedValue({ data: "Mocked Data" }),
    };

    return {
      createPromiseClient: vi.fn(() => mockClient),
    };
  });

  function mountWrapper(ingredient): VueWrapper<any, any> {
    return mount(Ingredient, {
      global: {
        plugins: [createVuetify({ components, directives })],
      },
      props: {
        item: ingredient,
      },
    });
  }

  afterEach(() => {
    vi.restoreAllMocks();
  });

  test("render simple ingredient", async () => {
    // Given
    const wrapper = await mountWrapper({
      name: "Test",
      quantity: 12,
      price: 123,
    });

    // Then
    expect(wrapper.find("[data-testid=ingredient-quantity-name]").text()).toBe(
      "12 X Test"
    );
    expect(wrapper.find("[data-testid=ingredient-rentability]").exists()).toBe(
      false
    );
    expect(
      wrapper.find("[data-testid=ingredient-fabrication-cost]").exists()
    ).toBe(false);
    expect(wrapper.find("[data-testid=ingredient-nb-object]").exists()).toBe(
      false
    );
  });

  test("render full ingredient", async () => {
    // Given
    const wrapper = await mountWrapper({
      name: "Test",
      quantity: 12,
      price: 123,
      rentabilite: 66,
      cout_fabrication: 12456,
      nb_objet: 4,
    });
    // Then
    expect(wrapper.find("[data-testid=ingredient-quantity-name]").text()).toBe(
      "12 X Test"
    );
    expect(wrapper.find("[data-testid=ingredient-rentability]").exists()).toBe(
      true
    );
    expect(
      wrapper.find("[data-testid=ingredient-fabrication-cost]").exists()
    ).toBe(true);
    expect(wrapper.find("[data-testid=ingredient-nb-object]").exists()).toBe(
      true
    );
  });

  test.each([
    [123, "123"],
    [1234, "1,2 k"],
    [12345, "12 k"],
    [123456, "123 k"],
    [1234567, "1,2 M"],
  ])("compute price %i -> %s", async (price: number, computedPrice: string) => {
    // Given
    const wrapper = mountWrapper({
      name: "Test",
      quantity: 12,
      price: price,
    });

    // Then
    expect(wrapper.vm.computedPrice).toBe(computedPrice);
  });

  test.each([
    [123, "123"],
    [1234, "1,2 k"],
    [12345, "12 k"],
    [123456, "123 k"],
    [1234567, "1,2 M"],
  ])(
    "compute estimated gain %i -> %s",
    async (gainEstime: number, computedEstimatedGain: string) => {
      // Given
      const wrapper = mountWrapper({
        name: "Test",
        quantity: 12,
        gain_estime: gainEstime,
      });

      // Then
      expect(wrapper.vm.computedEstimatedGain).toBe(computedEstimatedGain);
    }
  );

  test.each([
    [123, "123"],
    [1234, "1,2 k"],
    [12345, "12 k"],
    [123456, "123 k"],
    [1234567, "1,2 M"],
  ])(
    "compute craft cost %i -> %s",
    async (coutFabrication: number, computedCraftCost: string) => {
      // Given
      const wrapper = mountWrapper({
        name: "Test",
        quantity: 12,
        cout_fabrication: coutFabrication,
      });

      // Then
      expect(wrapper.vm.computedCraftCost).toBe(computedCraftCost);
    }
  );

  test("update ingredient price", async () => {
    // Given
    const wrapper = await mountWrapper({
      name: "Test",
      quantity: 12,
      price: 123,
    });

    // When
    const input = wrapper.find("[data-testid=ingredient-price] input");
    await input.setValue(456);
    await input.trigger("change");

    // Then
    expect(createPromiseClient().update).toHaveBeenCalledWith({
      name: "Test",
      price: "456",
    });
  });

  test.each([
    [-10, "red"],
    [19, "orange"],
    [53, "green"],
  ])(
    "check rentability color %i -> %s",
    async (rentability: number, expectedColor: string) => {
      // Given
      const wrapper = await mountWrapper({
        name: "Test",
        quantity: 12,
        rentabilite: rentability,
      });

      // Then
      expect(wrapper.vm.getColor(rentability)).toBe(expectedColor);
    }
  );

  test.each([
    ["123", 123],
    ["1 k", 1000],
  ])(
    "reverse formatting %s -> %i",
    async (formattedValue: string, value: number) => {
      // Given
      const wrapper = await mountWrapper({
        name: "Test",
        quantity: 12,
      });

      // Then
      expect(wrapper.vm.reverseFormatting(formattedValue)).toBe(value);
    }
  );
});
