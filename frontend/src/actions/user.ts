"use server";

import {
  ApiResult,
  CreateUserData,
  UpdateUserData,
  DeleteUserData,
  ReadUserData,
  LoginUserData,
} from "@/types/response";
import { safeParseJson } from "@/utils/utility";

export async function createUser(
  formData: FormData
): Promise<ApiResult<CreateUserData>> {
  const formObject = Object.fromEntries(formData.entries());

  const response = await fetch(`${process.env.BASE_URL}/api/user`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formObject),
  });

  return await safeParseJson(response);
}

export async function updateUser(
  formData: FormData
): Promise<ApiResult<UpdateUserData>> {
  const formObject = Object.fromEntries(formData.entries());

  const response = await fetch(`${process.env.BASE_URL}/api/user`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formObject),
  });

  return await safeParseJson(response);
}

export async function deleteUser(
  formData: FormData
): Promise<ApiResult<DeleteUserData>> {
  const formObject = Object.fromEntries(formData.entries());

  const response = await fetch(`${process.env.BASE_URL}/api/user`, {
    method: "DELETE",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formObject),
  });

  return await safeParseJson(response);
}

export async function readUser(
  formData: FormData
): Promise<ApiResult<ReadUserData>> {
  const formObject = Object.fromEntries(formData.entries());

  const response = await fetch(`${process.env.BASE_URL}/api/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formObject),
  });

  return await safeParseJson(response);
}

export async function loginUser(
  formData: FormData
): Promise<ApiResult<LoginUserData>> {
  const formObject = Object.fromEntries(formData.entries());

  const response = await fetch(`${process.env.BASE_URL}/api/user/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formObject),
  });

  return await safeParseJson(response);
}
