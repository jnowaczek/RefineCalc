SELECT t1.typeID, t1.typeName, invGroups.categoryID, invGroups.groupName, invTypeMaterials.materialTypeID, t2.typeName, invTypeMaterials.quantity
FROM invGroups
JOIN invTypes t1 on t1.groupID = invGroups.groupID
LEFT OUTER JOIN invTypeMaterials on invTypeMaterials.typeID = t1.typeID
LEFT OUTER JOIN invTypes t2 on invTypeMaterials.materialTypeID = t2.typeID
WHERE invGroups.categoryID = 25 -- Asteroids or something