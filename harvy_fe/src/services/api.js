import axios from 'axios';
import store from '@/store';

// api를 heroku에서 불러오도록 경로 추가
const API_BASE_URL = process.env.VUE_APP_VITE_API_BASE_URL || 'https://harvy-dev-f064f0b3b0ee.herokuapp.com/api/';
console.log('API_BASE_URL:', API_BASE_URL);

const api = axios.create({
    // baseURL: process.env.VUE_APP_API_URL || 'http://localhost:8000/api/',
    baseURL: API_BASE_URL,
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
    },
});

// 요청 인터셉터
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('token');
        if (token) {
            config.headers['Authorization'] = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

// 응답 인터셉터
api.interceptors.response.use(
    (response) => response,
    async (error) => {
        if (error.response && error.response.status === 401 && error.config && !error.config.__isRetryRequest) {
            try {
                await store.dispatch('auth/refreshToken');
                error.config.__isRetryRequest = true;
                return api(error.config);
            } catch (refreshError) {
                return Promise.reject(refreshError);
            }
        }
        return Promise.reject(error);
    }
);

// 로그인 함수
api.login = async (credentials) => {
    const response = await api.post('auth/login/', credentials);
    if (response.data.access) {
        localStorage.setItem('token', response.data.access);
    }
    return response.data;
};

// 회원가입 함수 추가
api.signup = async (formData) => {
    const response = await api.post('auth/signup/', formData); // 회원가입 API 호출
    return response.data;
};

// 관리자 확인 함수
api.checkAdmin = async () => {
    const response = await api.get('check-admin/');
    return response.data.isAdmin;
};

export default api;
