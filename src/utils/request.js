import axios from 'axios'
import qs from 'qs'

const request = axios.create({
  baseURL: 'http://127.0.0.1:8080',
  timeout: 5000,
  headers: {
    'Content-Type':
      'application/x-www-form-urlencoded;charset=UTF-8'
  }
})

request.interceptors.request.use(
  config => {
    if (config.method === 'post') {
      config.data = qs.stringify(config.data)
      config.headers = {
        'Content-Type':
          'application/x-www-form-urlencoded;charset=UTF-8'
      }
    }
    // if (localStorage.token) {
    //   config.headers.Authorization =
    //     'Bearer ' + localStorage.token
    // }
    return config
  },
  error => {
    return Promise.reject(error)
  }
)

request.interceptors.response.use(
  response => {
    return response
  },
  error => {
    return Promise.reject(error)
  }
)

export default request
