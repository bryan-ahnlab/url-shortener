export interface ApiErrorShape {
  type: string;
  title: string;
  status: number;
  detail: string;
  instance: string;
  method: string;
}

export class ApiError extends Error implements ApiErrorShape {
  type: string;
  title: string;
  status: number;
  detail: string;
  instance: string;
  method: string;

  constructor(params: ApiErrorShape) {
    super(params.detail);
    this.name = "ApiError";

    this.type = params.type;
    this.title = params.title;
    this.status = params.status;
    this.detail = params.detail;
    this.instance = params.instance;
    this.method = params.method;
  }

  toJSON(): ApiErrorShape {
    const { type, title, status, detail, instance, method } = this;
    return { type, title, status, detail, instance, method };
  }
}

export const DEFAULT_API_ERROR: ApiErrorShape = {
  type: "about:blank",
  title: "API Error",
  status: 500,
  detail: "DEFAULT_API_ERROR",
  instance: "",
  method: "",
};
