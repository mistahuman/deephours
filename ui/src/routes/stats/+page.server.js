import { fetchData } from '../../lib/utils/api.js';

export const load = async ({ params }) => {
	const resp = await fetchData('stats/');
	const stats = resp.stats;
	return {
		stats
	};
};
