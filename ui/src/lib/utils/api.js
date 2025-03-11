import { PUBLIC_API_URL } from '$env/static/public';
import { browser } from '$app/environment';

// Per richieste client-side, usa la route del proxy Nginx
export async function fetchData(endpoint) {
    const baseUrl = browser ? '' : 'http://backend:8000';
    const url = browser ? `/api/${endpoint}` : `${baseUrl}/${endpoint}`;

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

export async function postData(endpoint, body) {
    const baseUrl = browser ? '/api' : 'http://backend:8000';
    
    try {
        const response = await fetch(`${baseUrl}/${endpoint}`, {
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

// Applica la stessa logica per patchData e deleteData
export async function patchData(endpoint, body) {
    const baseUrl = browser ? '/api' : 'http://backend:8000';
    
    try {
        const response = await fetch(`${baseUrl}/${endpoint}`, {
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

export async function deleteData(endpoint) {
    const baseUrl = browser ? '/api' : 'http://backend:8000';
    
    try {
        const response = await fetch(`${baseUrl}/${endpoint}`, {
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