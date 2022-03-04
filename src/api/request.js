// axios 二次封装
import axios from 'axios';

// 创建 axios 实例
const requests = axios.create({
  baseURL: 'http://127.0.0.1:5700',
  timeout: 5000
});

// 请求拦截器, 请求前处理数据
requests.interceptors.request.use(config => {
  return config;
});

// 响应拦截器, 返回数据进行处理
requests.interceptors.response.use(
  res => {
    return res.data;
  },
  error => {
    return Promise.reject();
  }
);

// 导出, 供外部调用
export default requests;
