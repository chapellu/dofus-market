// @generated by protoc-gen-connect-es v0.13.0 with parameter "target=ts"
// @generated from file grpc_market.proto (package dofus_market.grpc_market, syntax proto3)
/* eslint-disable */
// @ts-nocheck

import { EquipementDetailsRequest, EquipementDetailsResponse, EquipementListRequest, EquipementListResponse, EquipementResponse, EquipementRetrieveRequest, IngredientDestroyRequest, IngredientForCraftDestroyRequest, IngredientForCraftListRequest, IngredientForCraftListResponse, IngredientForCraftPartialUpdateRequest, IngredientForCraftRequest, IngredientForCraftResponse, IngredientForCraftRetrieveRequest, IngredientListRequest, IngredientListResponse, IngredientPartialUpdateRequest, IngredientRequest, IngredientResponse, IngredientRetrieveRequest, MetierDestroyRequest, MetierListRequest, MetierListResponse, MetierPartialUpdateRequest, MetierRequest, MetierResponse, MetierRetrieveRequest, RecetteDestroyRequest, RecetteListRequest, RecetteListResponse, RecettePartialUpdateRequest, RecetteRequest, RecetteResponse, RecetteRetrieveRequest, RuneDestroyRequest, RuneListRequest, RuneListResponse, RunePartialUpdateRequest, RuneRequest, RuneResponse, RuneRetrieveRequest } from "./grpc_market_pb.js";
import { Empty, MethodKind } from "@bufbuild/protobuf";

/**
 * @generated from service dofus_market.grpc_market.EquipementController
 */
export const EquipementController = {
  typeName: "dofus_market.grpc_market.EquipementController",
  methods: {
    /**
     * @generated from rpc dofus_market.grpc_market.EquipementController.Details
     */
    details: {
      name: "Details",
      I: EquipementDetailsRequest,
      O: EquipementDetailsResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.EquipementController.List
     */
    list: {
      name: "List",
      I: EquipementListRequest,
      O: EquipementListResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.EquipementController.Retrieve
     */
    retrieve: {
      name: "Retrieve",
      I: EquipementRetrieveRequest,
      O: EquipementResponse,
      kind: MethodKind.Unary,
    },
  }
} as const;

/**
 * @generated from service dofus_market.grpc_market.IngredientController
 */
export const IngredientController = {
  typeName: "dofus_market.grpc_market.IngredientController",
  methods: {
    /**
     * @generated from rpc dofus_market.grpc_market.IngredientController.Create
     */
    create: {
      name: "Create",
      I: IngredientRequest,
      O: IngredientResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.IngredientController.Destroy
     */
    destroy: {
      name: "Destroy",
      I: IngredientDestroyRequest,
      O: Empty,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.IngredientController.List
     */
    list: {
      name: "List",
      I: IngredientListRequest,
      O: IngredientListResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.IngredientController.PartialUpdate
     */
    partialUpdate: {
      name: "PartialUpdate",
      I: IngredientPartialUpdateRequest,
      O: IngredientResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.IngredientController.Retrieve
     */
    retrieve: {
      name: "Retrieve",
      I: IngredientRetrieveRequest,
      O: IngredientResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.IngredientController.Update
     */
    update: {
      name: "Update",
      I: IngredientRequest,
      O: IngredientResponse,
      kind: MethodKind.Unary,
    },
  }
} as const;

/**
 * @generated from service dofus_market.grpc_market.IngredientForCraftController
 */
export const IngredientForCraftController = {
  typeName: "dofus_market.grpc_market.IngredientForCraftController",
  methods: {
    /**
     * @generated from rpc dofus_market.grpc_market.IngredientForCraftController.Create
     */
    create: {
      name: "Create",
      I: IngredientForCraftRequest,
      O: IngredientForCraftResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.IngredientForCraftController.Destroy
     */
    destroy: {
      name: "Destroy",
      I: IngredientForCraftDestroyRequest,
      O: Empty,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.IngredientForCraftController.List
     */
    list: {
      name: "List",
      I: IngredientForCraftListRequest,
      O: IngredientForCraftListResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.IngredientForCraftController.PartialUpdate
     */
    partialUpdate: {
      name: "PartialUpdate",
      I: IngredientForCraftPartialUpdateRequest,
      O: IngredientForCraftResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.IngredientForCraftController.Retrieve
     */
    retrieve: {
      name: "Retrieve",
      I: IngredientForCraftRetrieveRequest,
      O: IngredientForCraftResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.IngredientForCraftController.Update
     */
    update: {
      name: "Update",
      I: IngredientForCraftRequest,
      O: IngredientForCraftResponse,
      kind: MethodKind.Unary,
    },
  }
} as const;

/**
 * @generated from service dofus_market.grpc_market.MetierController
 */
export const MetierController = {
  typeName: "dofus_market.grpc_market.MetierController",
  methods: {
    /**
     * @generated from rpc dofus_market.grpc_market.MetierController.Create
     */
    create: {
      name: "Create",
      I: MetierRequest,
      O: MetierResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.MetierController.Destroy
     */
    destroy: {
      name: "Destroy",
      I: MetierDestroyRequest,
      O: Empty,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.MetierController.List
     */
    list: {
      name: "List",
      I: MetierListRequest,
      O: MetierListResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.MetierController.PartialUpdate
     */
    partialUpdate: {
      name: "PartialUpdate",
      I: MetierPartialUpdateRequest,
      O: MetierResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.MetierController.Retrieve
     */
    retrieve: {
      name: "Retrieve",
      I: MetierRetrieveRequest,
      O: MetierResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.MetierController.Update
     */
    update: {
      name: "Update",
      I: MetierRequest,
      O: MetierResponse,
      kind: MethodKind.Unary,
    },
  }
} as const;

/**
 * @generated from service dofus_market.grpc_market.RecetteController
 */
export const RecetteController = {
  typeName: "dofus_market.grpc_market.RecetteController",
  methods: {
    /**
     * @generated from rpc dofus_market.grpc_market.RecetteController.Create
     */
    create: {
      name: "Create",
      I: RecetteRequest,
      O: RecetteResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.RecetteController.Destroy
     */
    destroy: {
      name: "Destroy",
      I: RecetteDestroyRequest,
      O: Empty,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.RecetteController.List
     */
    list: {
      name: "List",
      I: RecetteListRequest,
      O: RecetteListResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.RecetteController.PartialUpdate
     */
    partialUpdate: {
      name: "PartialUpdate",
      I: RecettePartialUpdateRequest,
      O: RecetteResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.RecetteController.Retrieve
     */
    retrieve: {
      name: "Retrieve",
      I: RecetteRetrieveRequest,
      O: RecetteResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.RecetteController.Update
     */
    update: {
      name: "Update",
      I: RecetteRequest,
      O: RecetteResponse,
      kind: MethodKind.Unary,
    },
  }
} as const;

/**
 * @generated from service dofus_market.grpc_market.RuneController
 */
export const RuneController = {
  typeName: "dofus_market.grpc_market.RuneController",
  methods: {
    /**
     * @generated from rpc dofus_market.grpc_market.RuneController.Create
     */
    create: {
      name: "Create",
      I: RuneRequest,
      O: RuneResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.RuneController.Destroy
     */
    destroy: {
      name: "Destroy",
      I: RuneDestroyRequest,
      O: Empty,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.RuneController.List
     */
    list: {
      name: "List",
      I: RuneListRequest,
      O: RuneListResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.RuneController.PartialUpdate
     */
    partialUpdate: {
      name: "PartialUpdate",
      I: RunePartialUpdateRequest,
      O: RuneResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.RuneController.Retrieve
     */
    retrieve: {
      name: "Retrieve",
      I: RuneRetrieveRequest,
      O: RuneResponse,
      kind: MethodKind.Unary,
    },
    /**
     * @generated from rpc dofus_market.grpc_market.RuneController.Update
     */
    update: {
      name: "Update",
      I: RuneRequest,
      O: RuneResponse,
      kind: MethodKind.Unary,
    },
  }
} as const;

