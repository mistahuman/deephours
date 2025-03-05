import { fetchData } from '$lib/utils/api.js';

export const load = async ({ params }) => {
    try {
        const resp_wls = await fetchData(`worklogs/`);
        const worklogs = resp_wls.worklogs || [];
        return {
            worklogs,
        };
    } catch (error) {
        console.error('Error loading worklogs:', error);
        return {
            worklogs: [],
        };
    }
};