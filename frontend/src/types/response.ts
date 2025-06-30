import { ApiError } from "@/types/error";

/* interface: object structure for convention  */
/* type: integrated api response for readability  */

interface ApiSuccess<T> {
  ok: true;
  data: T;
}

interface ApiFailure {
  ok: false;
  error: ApiError;
}

export type ApiResult<T> = ApiSuccess<T> | ApiFailure;

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
