import { fetchData } from '$lib/utils/api.js';

export const load = async ({ params }) => {
    try {
        const resp_wls = await fetchData(`worklogs/${params.month}`);
        const worklogs = resp_wls.worklogs || [];
        const resp_proj = await fetchData(`projects/`);
        const projects = resp_proj.projects || [];
        console.log(projects);
        return {
            worklogs,
            projects
        };
    } catch (error) {
        console.error('Error loading worklogs:', error);
        return {
            worklogs: [],
            projects: []
        };
    }
};