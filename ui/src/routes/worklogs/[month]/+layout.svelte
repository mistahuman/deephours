<script>
	import { fetchData, postData, patchData, deleteData } from '$lib/utils/api.js';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	
	let selectedMonth = $page.params.month || new Date().toISOString().slice(0, 7);

	function handleMonthChange(event) {
		selectedMonth = event.target.value;
		goto(`/worklogs/${selectedMonth}`);
	}


</script>

<div class="card w-full text-token">
	<header class="card-header h5">Select month date:</header>
	<section class="p-4 space-y-4">
		<div class="grid grid-cols-3 gap-8">
			<input
				class="input"
				title=""
				type="month"
				bind:value={selectedMonth}
				on:change={handleMonthChange}
			/>
		</div>
	</section>
	<!-- <div class="p-4">
		<a href="/worklogs/{selectedMonth}" class="btn btn-md variant-ghost-surface">Go to worklogs</a>
	</div> -->
</div>

<slot />