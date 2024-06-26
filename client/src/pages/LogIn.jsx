import { useForm } from 'react-hook-form';
import * as yup from 'yup';
import { yupResolver } from '@hookform/resolvers/yup';
import useAuth from '@/hooks/customs/useAuth';
import { useNavigate } from 'react-router-dom';

const schema = yup
	.object()
	.shape({
		email: yup
			.string()
			.email('Invalid email')
			.required('Email is required'),
		password: yup.string().required('Password is required'),
	})
	.required();

const LogIn = () => {
	const {
		register,
		handleSubmit,
		formState: { errors },
	} = useForm({
		resolver: yupResolver(schema),
	});

	const { login, isAuthenticated } = useAuth();
	const navigate = useNavigate();

	const onSubmit = async (data) => {
		const success = await login(data.email, data.password);

		success && (isAuthenticated() ?? navigate('/'))
	};

	return (
		<section>
			<h2>Log In</h2>
			<form onSubmit={handleSubmit(onSubmit)}>
				<div className='form-group'>
					<label>Email</label>
					<input
						type='email'
						{...register('email')}
					/>
					{errors.email && (
						<span>
							{errors.email.message}
						</span>
					)}
				</div>
				<div className='form-group'>
					<label>Password</label>
					<input
						type='password'
						{...register('password')}
					/>
					{errors.password && (
						<span>
							{
								errors.password
									.message
							}
						</span>
					)}
				</div>
				<button type='submit'>Log In</button>
			</form>
		</section>
	);
};

export default LogIn;
