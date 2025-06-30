export class ApiError extends Error {
  type: string;
  title: string;
  status: number;
  detail: string;
  instance: string;
  method: string;

  constructor({
    type,
    title,
    status,
    detail,
    instance,
    method,
  }: {
    type: string;
    title: string;
    status: number;
    detail: string;
    instance: string;
    method: string;
  }) {
    super(detail);
    this.name = "ApiError";
    this.type = type;
    this.title = title;
    this.status = status;
    this.detail = detail;
    this.instance = instance;
    this.method = method;
  }

  toJSON() {
    return {
      type: this.type,
      title: this.title,
      status: this.status,
      detail: this.detail,
      instance: this.instance,
      method: this.method,
    };
  }
}

export const DEFAULT_API_ERROR = {
  type: "about:blank",
  title: "API Error",
  status: 500,
  detail: "DEFAULT_API_ERROR",
  instance: "",
  method: "",
};
