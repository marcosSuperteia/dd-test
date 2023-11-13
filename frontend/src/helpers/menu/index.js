export const getMenuData = [
    {
      title: 'Dashboards',
      key: 'dashboards',
      icon: 'pi pi-home',
      count: 1,
      children: [
        {
          title: 'Dashboard home',
          key: 'dashboardHome',
          url: '/dashboard/home',
        },       
      ],
    },
    {
      title: 'Auth Pages',
      key: 'auth',
      icon: 'pi pi-user',
      count: 1,
      children: [
        {
          title: 'User',
          key: 'user',
          url: '/user',
        },
        {
          title: 'Role',
          key: 'role',
          url: '/role',
        },
      ],
    },
  ]
  