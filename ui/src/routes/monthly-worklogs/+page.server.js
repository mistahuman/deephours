import { fetchData } from '../../lib/utils/api.js';

export const load = async ({ params }) => {
	const resp_proj = await fetchData('projects/');
	const projects = resp_proj.projects;
	return {
		projects
	};
};
