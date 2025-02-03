<script>
	export let data;
	import IconKit from '$lib/components/IconKit.svelte';
	import { Modal, getModalStore } from '@skeletonlabs/skeleton';
	import ModalDelete from '$lib/components/ModalDelete.svelte';
	import ModalProject from '$lib/components/ModalProject.svelte';
	import { postData, patchData, deleteData } from '$lib/utils/api.js';
	import { getToastStore } from '@skeletonlabs/skeleton';
	import { popup } from '@skeletonlabs/skeleton';

	const toastStore = getToastStore();
	const modalStore = getModalStore();

	let { projects } = data;
	let newProject = {
		// title: "Sample title",
		// code: "SAMPLECODE",
		// description: "Sample description"
	};

	// Add project
	function saveProject(project) {
		const modalComponent = {
			ref: ModalProject
		};
		const modal = {
			type: 'component',
			component: modalComponent,
			title: 'Add Project',
			body: 'Fill out the form to add a project',
			formdata: project,
			response: (r) => apiAddProject(r)
		};
		modalStore.trigger(modal);
	}

	async function apiAddProject(r) {
		let message = 'Error! Project not added.';
		let type = 'variant-filled-error';
		if (r) {
			try {
				const response = await postData('projects/', r);
				if (response) {
					type = 'variant-filled-success';
					message = 'Project added successfully';
					projects = [...projects, response];
				}
				console.log(response);
			} catch (error) {
				console.log(error);
			}
		} else {
			type = 'variant-filled-warning';
			message = 'Project addition canceled';
		}
		const toast = {
			message: message,
			timeout: 10000,
			background: type
		};
		toastStore.trigger(toast);
	}

	// Edit project
	function editProject(proj) {
		const modalComponent = {
			ref: ModalProject
		};
		const modal = {
			type: 'component',
			component: modalComponent,
			title: 'Edit Project: ' + proj.code,
			body: '',
			formdata: proj,
			response: (r) => apiPatchProject(proj.id, r)
		};
		modalStore.trigger(modal);
	}

	async function apiPatchProject(projId, body) {
		let message = 'Error! Project not updated.';
		let type = 'variant-filled-error';
		if (body) {
			try {
				const response = await patchData('projects/' + projId, body);
				if (response) {
					type = 'variant-filled-success';
					message = 'Project updated successfully';
					const projectIndex = projects.findIndex((project) => project.id === projId);
					if (projectIndex !== -1) {
						projects[projectIndex] = response;
					}
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

	// Delete project
	function deleteProject(project) {
		const modalComponent = {
			ref: ModalDelete
		};
		const modal = {
			component: modalComponent,
			type: 'component',
			title: `Deleting project: ${project.title} (${project.code})`,
			body: 'Are you sure?',
			response: (r) => apiDeleteProject(project.id, project, r)
		};
		modalStore.trigger(modal);
	}

	async function apiDeleteProject(projId, body, resCancel) {
		let message = 'Error! Project not deleted.';
		let type = 'variant-filled-error';
		if (resCancel) {
			try {
				const response = await deleteData('projects/' + projId);
				if (response.status) {
					type = 'variant-filled-success';
					message = 'Project deleted successfully';
					const projectIndex = projects.findIndex((project) => project.id === body.id);
					if (projectIndex !== -1) {
						projects = projects;
						projects.splice(projectIndex, 1);
					}
				}
				console.log(response);
			} catch (error) {
				console.log(error);
			}
		} else {
			type = 'variant-filled-warning';
			message = 'Deletion canceled';
		}
		const toast = {
			message: message,
			timeout: 10000,
			background: type
		};
		toastStore.trigger(toast);
	}

	// Search
	let searchTerm = '';

	$: filteredTableData = projects.filter(
		(item) =>
			item.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
			item.code.toLowerCase().includes(searchTerm.toLowerCase())
	);
</script>

<h3 class="h3">Project List</h3>
<hr />
<div class="card">
	<header class="card-header flex justify-center">
		<div class="input-group input-group-divider grid-cols-[auto_1fr_auto]">
			<div class="input-group-shim">
				<IconKit name="mdi:magnify" />
			</div>
			<input type="search" placeholder="Search projects" bind:value={searchTerm} />
		</div>
		<div class="ml-2">
			<button class="btn btn-md variant-ghost-surface" on:click={() => saveProject(newProject)}
				><span>Add project</span></button
			>
		</div>
	</header>
	{#if projects.length}
		<section class="p-4">
			<div class="table-container">
				<!-- Native Table Element -->
				<table class="table table-hover">
					<thead>
						<tr>
							<th>Code</th>
							<th>Title</th>
							<th>Description</th>
							<th>Actions</th>
						</tr>
					</thead>
					<tbody>
						{#each filteredTableData as proj (proj.id)}
							<tr>
								<td>{proj.code}</td>
								<td>{proj.title}</td>
								<td>{proj.description}</td>
								<td>
									<button
										class="btn btn-sm variant-ghost-surface [&>*]:pointer-events-none"
										on:click={() => editProject(proj)}
										use:popup={{ event: 'hover', target: 'edit' + proj.code, placement: 'top' }}
										><span><IconKit name="mdi:pencil" /></span></button
									>
									<div class="card p-2 variant-filled-secondary" data-popup={'edit' + proj.code}>
										<p>Edit project</p>
										<div class="arrow variant-filled-secondary" />
									</div>
									<button
										class="btn btn-sm variant-ghost-surface [&>*]:pointer-events-none"
										on:click={() => deleteProject(proj)}
										use:popup={{ event: 'hover', target: 'delete' + proj.code, placement: 'top' }}
										><span><IconKit name="mdi:delete" /></span></button
									>
									<div class="card p-2 variant-filled-secondary" data-popup={'delete' + proj.code}>
										<p>Delete project</p>
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
		<section class="p-4 text-center">
			<h5 class="h5">List projects empty</h5>
		</section>
	{/if}
	<footer class="card-footer flex justify-center items-center">
		<!-- TODO pagination -->
	</footer>
</div>
