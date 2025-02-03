<script>
	export let data;
	import { ConicGradient } from '@skeletonlabs/skeleton';
	import { ProgressBar } from '@skeletonlabs/skeleton';

	let { stats } = data;
	const conicStops = [
		{ label: 'One', color: 'rgb(var(--color-success-500))', start: 0, end: 10 },
		{ label: 'Two', color: 'rgb(var(--color-secondary-500))', start: 10, end: 35 },
		{ label: 'Three', color: 'rgb(var(--color-primary-500))', start: 35, end: 100 }
	];
</script>

<h3 class="h3">Statistics</h3>
<hr />
<div class="card">
	<header class="card-header h2" />
	<section class="p-4">
		<div class="grid grid-cols-2 gap-8">
			<ConicGradient stops={stats} legend width="w-60">Worked hours by project</ConicGradient>
			<div class="p-4 space-y-4">
				<div class="h4">Total hours</div>
				<hr />
				{#each stats as proj}
					<div class="h5">{proj.label}: <strong>{proj.total_hours}h</strong></div>
					<ProgressBar
						meter="bg-secondary-500"
						track="bg-secondary-500/30"
						value={proj.perc}
						max={100}
					/>
				{/each}
			</div>
		</div>
	</section>
	<footer class="card-footer" />
</div>
