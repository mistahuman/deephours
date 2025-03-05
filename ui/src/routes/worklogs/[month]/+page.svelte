<script>
	export let data;

	import { formatDateLocale, formatMonthLocale } from '$lib/utils/utils.js';
	import IconKit from '$lib/components/IconKit.svelte';
	import { fetchData, postData, patchData, deleteData } from '$lib/utils/api.js';
	import { page } from '$app/stores';
	import { Modal, getModalStore } from '@skeletonlabs/skeleton';
	import ModalDelete from '$lib/components/ModalDelete.svelte';
	import ModalWorklog from '$lib/components/ModalWorklog.svelte';
	import { popup } from '@skeletonlabs/skeleton';
	import { getToastStore } from '@skeletonlabs/skeleton';
	import { invalidateAll } from '$app/navigation';

	const toastStore = getToastStore();
	const modalStore = getModalStore();

    // Get current month from URL parameter
    $: currentMonth = $page.params.month || new Date().toISOString().slice(0, 7);
    $: worklogs = data.worklogs || [];
    $: projects = data.projects || [];
    $: console.log('Page data received:', worklogs, projects);

    // search
	let searchTerm = '';

    $: filteredTableData = worklogs.filter((item) =>
        item.day?.toLowerCase().includes(searchTerm.toLowerCase()) || 
        item.project?.title?.toLowerCase().includes(searchTerm.toLowerCase()) ||
        item.descr?.toLowerCase().includes(searchTerm.toLowerCase())
    ).sort((a, b) => new Date(a.date) - new Date(b.date)); 

	let newWorklog = {};

	// Add project
	function saveWorklog(worklog) {
		const modalComponent = {
			ref: ModalWorklog
		};
		const modal = {
			type: 'component',
			component: modalComponent,
			title: 'Add worklog',
			body: 'Fill out the form to add a worklog',
			formdata: worklog,
			projects: projects,
			response: (r) => apiAddWorklog(r)
		};
		modalStore.trigger(modal);
	}

	async function apiAddWorklog(r) {
		let message = 'Error! Worklog not added.';
		let type = 'variant-filled-error';
		if (r) {
			try {
				const response = await postData('worklogs/', r);
				if (response) {
					type = 'variant-filled-success';
					message = 'Worklog added successfully';
					await invalidateAll();
				}
				console.log(response);
			} catch (error) {
				console.log(error);
			}
		} else {
			type = 'variant-filled-warning';
			message = 'Worklog addition canceled';
		}
		const toast = {
			message: message,
			timeout: 10000,
			background: type
		};
		toastStore.trigger(toast);
	}

	//edit
	function editWorklog(wl) {
		const modalComponent = {
			ref: ModalWorklog
		};
		const modal = {
			type: 'component',
			// Pass the component directly:
			component: modalComponent,
			title: 'Edit Worklog: ' + formatDateLocale(wl.day),
			body: '',
			formdata: wl,
			projects: projects,
			response: (r) => apiPatchWorklog(wl.id, r)
		};
		modalStore.trigger(modal);
	}

	async function apiPatchWorklog(wl_id, body) {
		let message = 'Error! Worklog not updated.';
		let type = 'variant-filled-error';
		if (body) {
			try {
				const response = await patchData('worklogs/' + wl_id, body);
				if (response) {
					type = 'variant-filled-success';
					message = 'Worklog updated successfully';
					await invalidateAll();
				}
				console.log(response);
			} catch (error) {
				console.log(error);
			}
		} else {
			type = 'variant-filled-warning';
			message = 'Edit canceled';
		}
		const toast = {
			message: message,
			timeout: 10000,
			background: type
		};
		toastStore.trigger(toast);
	}

	// delete
	function deleteWorklog(wl) {
		const modalComponent = {
			ref: ModalDelete
		};
		const modal = {
			component: modalComponent,
			type: 'component',
			title: `Deleting worklog: ${formatDateLocale(wl.day)}`,
			body: 'Are you sure?',
			response: (r) => apiDeleteWorklog(wl.id, wl, r)
		};
		modalStore.trigger(modal);
	}

	async function apiDeleteWorklog(projId, body, resCancel) {
		let message = 'Error! Worklog not deleted.';
		let type = 'variant-filled-error';
		if (resCancel) {
			try {
				const response = await deleteData('worklogs/' + projId);
				if (response.status) {
					type = 'variant-filled-success';
					message = 'Worklog deleted successfully';
					// aggiorno la lista
					const wlIndex = worklogs.findIndex((worklog) => worklog.id === body.id);
					if (wlIndex !== -1) {
						worklogs = worklogs;
						worklogs.splice(wlIndex, 1);
					}
				}
				console.log(response);
			} catch (error) {
				console.log(error);
			}
		} else {
			type = 'variant-filled-warning';
			message = 'Delete canceled';
		}
		const toast = {
			message: message,
			timeout: 10000,
			background: type
		};
		toastStore.trigger(toast);
	}
</script>

<div class="card w-full text-token">
	<header class="card-header">
		<div class="space-y-4">
			<h2 class="h2">{formatMonthLocale(currentMonth)}</h2>
			<div class="grid grid-cols-2 gap-4">
				<div class="input-group input-group-divider grid-cols-[auto_1fr_auto]">
					<div class="input-group-shim">
						<IconKit name="mdi:magnify" />
					</div>
					<input type="search" placeholder="Search worklogs" bind:value={searchTerm} />
				</div>
				<div class="ml-2">
					<button class="btn btn-md variant-ghost-surface" on:click={() => saveWorklog(newWorklog)}
						><span>Add worklog</span></button
					>
				</div>
			</div>
		</div>
	</header>
	{#if worklogs.length}
		<section class="p-4 space-y-4">
			<div class="table-container">
				<!-- Native Table Element -->
				<table class="table table-hover">
					<thead>
						<tr>
							<th>Day</th>
							<th>Project</th>
							<th>Worked hours</th>
							<th>Description</th>
							<th>Actions</th>
						</tr>
					</thead>
					<tbody>
						{#each filteredTableData as wl (wl.id)}
							<tr>
								<td>{formatDateLocale(wl.day)}</td>
								<td>{wl.project?.title} ({wl.project?.code})</td>
								<td>{wl.worked_hours}</td>
								<td>{wl.descr}</td>
								<td>
									<button
									class="btn btn-sm variant-ghost-surface [&>*]:pointer-events-none"
									on:click={() => editWorklog(wl)}
									use:popup={{ event: 'hover', target: "edit"+wl.code, placement: 'top' }}
									><span><IconKit name="mdi:pencil" /></span></button
								>
								<div class="card p-2 variant-filled-secondary" data-popup={"edit"+wl.code}>
									<p>Edit worklog</p>
									<div class="arrow variant-filled-secondary" />
								</div>
									<button
										class="btn btn-sm variant-ghost-surface [&>*]:pointer-events-none"
										on:click={() => deleteWorklog(wl)}
										use:popup={{ event: 'hover', target: 'delete' + wl.code, placement: 'top' }}
										><span><IconKit name="mdi:delete" /></span></button
									>
									<div class="card p-2 variant-filled-secondary" data-popup={'delete' + wl.code}>
										<p>Delete worklog</p>
										<div class="arrow variant-filled-secondary" />
									</div>
								</td>
							</tr>
						{/each}
					</tbody>
					<tfoot />
				</table>
			</div>
		</section>
	{:else}
		<section class="p-4">
			<p>No worklogs found for this month.</p>
		</section>
	{/if}
	<footer class="card-footer flex justify-center items-center">
		<!-- TODO pagination -->
	</footer>
</div>