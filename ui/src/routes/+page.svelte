<script>
	import NavCard from '$lib/components/NavCard.svelte';
	import { routes } from '$lib/utils/routes.js';
</script>

<div class="container h-full mx-auto flex justify-center items-center">
	<div class="space-y-10 text-center flex-col items-center">
		<h2 class="h2">Welcome to DeepHours.</h2>
		<p>Dive deep into your work statistics.</p>
		<div class="p-4 space-y-4">
			<div class="grid grid-cols-3 gap-4">
				{#each routes as card (card.href)}
					<NavCard title={card.title} content={card.content} href={card.href} icon={card.icon} />
				{/each}
			</div>
		</div>
	</div>
</div>

<style lang="postcss">
</style>
