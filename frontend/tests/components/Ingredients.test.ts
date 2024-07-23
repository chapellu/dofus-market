import { afterEach, describe, expect, test, vi } from "vitest";
import { mount, VueWrapper } from "@vue/test-utils";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import { createPromiseClient } from "@connectrpc/connect";
import Ingredients from "@/components/Ingredients.vue";

describe("Ingredients", () => {
  function mountWrapper(ingredients: Array<any>): VueWrapper<any, any> {
    return mount(Ingredients, {
      global: {
        plugins: [createVuetify({ components, directives })],
      },
      props: {
        ingredients: ingredients,
      },
    });
  }

  afterEach(() => {
    vi.restoreAllMocks();
  });

  test("render simple and full ingredients", async () => {
    // Given
    const wrapper = await mountWrapper([
      {
        name: "Test1",
        quantity: 12,
        price: 123,
      },
      {
        name: "Test2",
        quantity: 42,
        price: 123,
        rentabilite: 66,
        cout_fabrication: 12456,
        nb_objet: 4,
      },
    ]);

    // Then
    expect(
      wrapper.findAll("[data-testid=ingredient-quantity-name]")[0].text()
    ).toBe("12 X Test1");
    expect(
      wrapper.findAll("[data-testid=ingredient-quantity-name]")[1].text()
    ).toBe("42 X Test2");
    expect(wrapper.findAll("[data-testid=ingredient-rentability]")).length(1);
    expect(wrapper.findAll("[data-testid=ingredient-fabrication-cost]")).length(
      1
    );
    expect(wrapper.findAll("[data-testid=ingredient-nb-object]")).length(1);
  });

  test("ingredients expand on click", async () => {
    // Given
    const wrapper = await mountWrapper([
      {
        name: "Test2",
        quantity: 42,
        price: 123,
        rentabilite: 66,
        cout_fabrication: 12456,
        nb_objet: 4,
        ingredients: [
          {
            name: "Test21",
            quantity: 1,
            price: 123,
          },
        ],
      },
    ]);

    // When
    await wrapper.get("[data-testid=ingredient]").trigger("click");

    // Then
    console.log(wrapper.html());
  });
});
