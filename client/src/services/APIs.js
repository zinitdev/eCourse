import { BASE_URL } from '@/constants/constants';
import axios from 'axios';

const axiosInstance = axios.create({
	baseURL: BASE_URL,
});

axiosInstance.defaults.headers.common['Content-Type'] = 'application/json';

export default axiosInstance;
