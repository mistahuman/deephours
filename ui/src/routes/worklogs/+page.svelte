<script>
    import { formatDateLocale, formatMonthLocale } from '$lib/utils/utils.js';
    export let data;

    function groupWorklogsByMonth(worklogs) {
        return Object.values(
            worklogs.reduce((acc, worklog) => {
                const month = worklog.day.slice(0, 7);
                
                if (!acc[month]) {
                    acc[month] = { 
                        month,
                        totalHours: 0,
                        tasks: []
                    };
                }
                
                acc[month].tasks.push({
                    id: worklog.id,
                    day: worklog.day,
                    desc: worklog.descr || "",  
                    hours: worklog.worked_hours,
                    project: worklog.project
                });
                
                acc[month].totalHours += worklog.worked_hours;
                
                return acc;
            }, {})
        );
    }

    $: worklogs = data.worklogs || [];
    $: monthlyWorklogs = groupWorklogsByMonth(worklogs);
    $: console.log(monthlyWorklogs);
</script>


<div class="grid grid-cols-3 gap-4">

    {#each monthlyWorklogs as wl}
    <a href="worklogs/{wl.month}" class="card p-1">
        <header class="card-header h4">{formatMonthLocale(wl.month)}</header>
        <section class="p-4">Total hours: {wl.totalHours}</section>
    </a>
    {/each}
</div>



