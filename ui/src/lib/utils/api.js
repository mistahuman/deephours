import { PUBLIC_API_URL } from '$env/static/public';
import { browser } from '$app/environment';

const baseUrl = PUBLIC_API_URL;

export async function fetchData(endpoint) {

	const baseUrl = browser ? '' : 'http://backend:8000';
	const url = browser ? endpoint : `${baseUrl}/${endpoint}`;

	try {
		const response = await fetch(url);
		if (!response.ok) {
			throw new Error('Error during request FETCH');
		}
		return await response.json();
	} catch (error) {
		console.error('Error FETCH:', error);
		throw error;
	}
}

export async function postData(url, body) {
	try {
		const response = await fetch(baseUrl + url, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(body)
		});

		if (!response.ok) {
			throw new Error('Error during request POST');
		}

		return await response.json();
	} catch (error) {
		console.error('Error POST:', error);
		throw error;
	}
}

export async function patchData(url, body) {
	try {
		const response = await fetch(baseUrl + url, {
			method: 'PATCH',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(body)
		});

		if (!response.ok) {
			throw new Error('Error during request PATCH');
		}

		return await response.json();
	} catch (error) {
		console.error('Error PATCH:', error);
		throw error;
	}
}

export async function deleteData(url) {
	try {
		const response = await fetch(baseUrl + url, {
			method: 'DELETE',
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok) {
			throw new Error('Error during request DELETE');
		}

		return response;
	} catch (error) {
		console.error('Error DELETE:', error);
		throw error;
	}
}
