import axios from 'axios'

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_SERVER_NAME,
})


apiClient.interceptors.request.use((request) => {
  const accessToken = JSON.parse(localStorage.getItem('token'))
  if (accessToken) {
    request.headers.Authorization = `Bearer ${accessToken}`
    request.headers.AccessToken = accessToken
  }
  return request
})

apiClient.interceptors.response.use(undefined, (error) => {
  // Errors handling
  const { response } = error
  console.log()
})

export default apiClient
