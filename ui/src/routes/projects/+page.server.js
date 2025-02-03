import { fetchData } from '../../lib/utils/api.js';

export const load = async ({ params }) => {
	const resp = await fetchData('projects/');
	const projects = resp.projects;
	return {
		projects
	};
};
