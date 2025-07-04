import { ApiErrorShape } from "@/types/error";

/* interface: object structure for convention  */
/* type: integrated api response for readability  */

interface ApiSuccess<T> {
  ok: true;
  data: T;
}

interface ApiFailure {
  ok: false;
  error: ApiErrorShape;
}

export type ApiResult<T> = ApiSuccess<T> | ApiFailure;

// 단축 URL 생성
export interface ShortenUrlData {
  status: number;
  message: string;
  request: {
    long_url: string;
    description: string | null;
  };
  response: {
    id: string;
    long_url: string;
    description: string | null;
    short_url: string;
    created_at: string;
  };
}

// 회원 정보 응답 타입
export interface UserResponse {
  id: string;
  email: string;
  password: string;
  name: string;
  phone: string;
  address: string;
  birth: string;
  created_at: string;
  updated_at: string;
}

// 회원 생성
export interface CreateUserData {
  status: number;
  message: string;
  request: {
    email: string;
    password: string;
    name: string;
    phone: string;
    address: string;
    birth: string;
  };
  response: UserResponse;
}

// 회원 정보 수정
export interface UpdateUserData {
  status: number;
  message: string;
  request: {
    id: string;
    email: string;
    password: string;
    name: string;
    phone: string;
    address: string;
    birth: string;
  };
  response: UserResponse;
}

// 회원 정보 삭제
export interface DeleteUserData {
  status: number;
  message: string;
  request: {
    id: string;
  };
  response: boolean;
}

// 회원 정보 조회
export interface ReadUserData {
  status: number;
  message: string;
  request: {
    email: string;
    password: string;
  };
  response: UserResponse;
}

// 로그인
export interface LoginUserData {
  status: number;
  message: string;
  request: {
    email: string;
    password: string;
  };
  response: UserResponse;
}
